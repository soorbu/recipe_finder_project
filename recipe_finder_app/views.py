from django.shortcuts import render, redirect
from .forms import UserForm, RecipeForm, IngredientForm, CategoryForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import modelform_factory
from .models import Recipe, Ingredient, Category
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password  # Import make_password


# Landing Page
def landing_page(request):
    return render(request, 'landing_page.html')

def home_page(request):
    return render(request, 'home_page.html')

from django.contrib.auth import authenticate, login

from django.contrib.auth.hashers import check_password
from recipe_finder_app.models import User

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting to authenticate user: {username}")  # Debug statement

        try:
            user = User.objects.get(username=username)
            # Check if the entered password matches the stored (hashed) password
            if check_password(password, user.password):
                print("Authentication success")
                login(request, user)  # Use Django's login to log in the user
                return redirect('home_page')  # Redirect to home_page after successful login
            else:
                messages.error(request, 'Invalid username or password')
                print("Authentication failed")
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            print("User does not exist")

    return render(request, 'login_page.html')



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to the database yet
            # Hash the password before saving
            user.password = make_password(form.cleaned_data['password'])
            user.save()  # Save the user with the hashed password
            return redirect('login_page')  # Redirect to login after successful registration
    else:
        form = UserForm()
    
    return render(request, 'create_account.html', {'form': form})




def handle_uploaded_file(f):
    file_path = os.path.join('static/media', f.name)  # Path where to save
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path  # Return the path to the saved file


def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        category_form = CategoryForm(request.POST)

        if recipe_form.is_valid() and category_form.is_valid():
            # Save recipe
            recipe = recipe_form.save(commit=False)

            # Only set imageurl if an image was uploaded
            if 'imageurl' in request.FILES:
                recipe.imageurl = handle_uploaded_file(request.FILES['imageurl'])

            recipe.userid = request.user  # Associate the recipe with the logged-in user
            recipe.save()

            # Save ingredients
            ingredients = request.POST.getlist('ingredient')  # Use getlist to get multiple ingredients
            for ingredient_name in ingredients:
                if ingredient_name:  # Check if ingredient is not empty
                    ingredient = Ingredient(recipeid=recipe, ingredient=ingredient_name.strip())
                    ingredient.save()

            # Save categories
            Category.objects.create(
                recipeid=recipe,
                cuisine_type=category_form.cleaned_data['cuisine_type'],
                meal_type=category_form.cleaned_data['meal_type'],
                dietary_restrictions=category_form.cleaned_data['dietary_restrictions'],
            )

            return redirect('home_page')  # Redirect after saving
        else:
            print(recipe_form.errors)
            print(category_form.errors)
    else:
        recipe_form = RecipeForm()
        category_form = CategoryForm()

    return render(request, 'addrecipe.html', {
        'recipe_form': recipe_form,
        'category_form': category_form,
    })

def handle_uploaded_file(f):
    file_path = os.path.join('static/media', f.name)  # Path where to save
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path  # Return the path to the saved file

def search_recipes(request):
    return render(request, 'search_recipes.html')

# View for Blog (My Recipes)
def my_recipes(request):
    return render(request, 'my_recipes.html')

# View for Adding a Recipe
def add_recipe(request):
    return render(request, 'addrecipe.html')

def logout_user(request):
    logout(request)
    return redirect('login_page')