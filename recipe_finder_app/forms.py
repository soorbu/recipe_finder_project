from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Recipe, Ingredient, Category

# Form for creating a new user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'name', 'password']

# Recipe Form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'imageurl']

# Ingredient Form
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient']

# Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cuisine_type', 'meal_type', 'dietary_restrictions']
