from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RecipeForm,RecipeIngredientForm
from .models import Recipe, Category, Ingredient, RecipeIngredient, Like
from django.db.models import Count, F, Q, Case, When, Subquery, OuterRef, Sum
from django.db import models
from django.db.models.functions import Lower



def landing_page(request):
    return render(request, 'landing_page.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')  
    return render(request, 'login_page.html')
        
def create_account(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            return redirect('login_page')  # Redirect to home page after sign-up
    else:
        form = SignUpForm()
    return render(request, 'create_account.html', {'form': form})
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Add this line
            form.save()
            return redirect('login_page')  # redirect to home page after successful signup
        else:
            print("Form is not valid!")  # Add this line
            print(form.errors)  # Add this line
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home_page(request):
    return render(request, 'home_page.html')

def index(request):
    return render(request,'index.html')

def logout_view(request):
    logout(request)
    return redirect('login_page')

from django.forms import formset_factory
@login_required
def add_recipe(request):
    RecipeIngredientFormSet = formset_factory(RecipeIngredientForm, extra=1)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        ingredient_formset = RecipeIngredientFormSet(request.POST)
        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            for form in ingredient_formset:
                if form.is_valid():
                    ingredient_name = form.cleaned_data.get('ingredient_name')
                    ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                    quantity = form.cleaned_data.get('quantity')
                    RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity)

            categories = request.POST.getlist('category')
            for category_id in categories:
                category = Category.objects.get(id=category_id)
                recipe.category.add(category)
            return redirect('my_recipes')
    else:
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()
    return render(request, 'add_recipe.html', {'recipe_form': recipe_form, 'ingredient_formset': ingredient_formset})

def search_recipes(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        search_by = request.POST.get('search_by')

        if search_by == 'title':
            recipes = Recipe.objects.annotate(
                keyword_score=Case(
                    When(title__icontains=keyword, then=1),
                    default=0,
                    output_field=models.IntegerField()
                ),
                likes_score=Count('likes'),
                combined_score=F('keyword_score') * 0.7 + F('likes_score') * 0.3
            ).filter(keyword_score__gte=1).order_by('-combined_score')
        elif search_by == 'ingredients':
            ingredient_ids = RecipeIngredient.objects.annotate(
                keyword_score=Case(
                    When(ingredient__name__icontains=keyword, then=1),
                    default=0,
                    output_field=models.IntegerField()
                )
            ).values('recipe_id', 'keyword_score')

            recipes = Recipe.objects.filter(id__in=Subquery(ingredient_ids.values('recipe_id'))).annotate(
                keyword_score=Sum('recipeingredient__keyword_score'),
                likes_score=Count('likes'),
                combined_score=F('keyword_score') * 0.4 + F('likes_score') * 0.6
            ).filter(keyword_score__gt=0).order_by('-combined_score')

        return render(request, 'search_results.html', {'recipes': recipes})
    else:
        return render(request, 'search.html')
def my_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'my_recipes.html', {'recipes': recipes})

@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('my_recipes')
    return redirect('my_recipes')

def like_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, recipe=recipe)
    if not created:
        like.delete()
    return redirect('recipe_details', pk=pk)

def search_results(request):
    if 'q' in request.GET:
        q = request.GET['q']
        recipes = Recipe.objects.filter(name__icontains=q)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'search_results.html', {'recipes': recipes})

def recipe_details(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_details.html', {'recipe': recipe})
