from django.shortcuts import render, redirect
from .forms import UserForm, RecipeForm, IngredientForm, CategoryForm
from .models import User
from django.contrib.auth import authenticate, login, logout

# Landing Page
def landing_page(request):
    return render(request, 'landing_page.html')

# Home Page
def home(request):
    return render(request, 'home.html')

# Success Page after User Registration
def success_user(request):
    return render(request, 'success_user.html')

# User Login
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home_page.html')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid credentials'})
    return render(request, 'login_page.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')  # Redirect to login after successful registration
    else:
        form = UserForm()
    return render(request, 'create_account.html', {'form': form})

# Recipe Creation
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_recipe')
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})

# Ingredient Creation
def create_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_ingredient')
    else:
        form = IngredientForm()
    return render(request, 'create_ingredient.html', {'form': form})

# Category Creation
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_category')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})
