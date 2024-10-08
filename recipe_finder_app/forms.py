from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from .models import User, Recipe, Ingredient, Category

# Form for creating a new user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'name', 'password']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'imageurl']
    
    imageurl = forms.ImageField(required=False)  # Optional image field

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("This field is required.")
        return title.strip().lower()

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return description.strip() if description else ""

    def clean_instructions(self):
        instructions = self.cleaned_data.get('instructions')
        return instructions.strip() if instructions else ""

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient']

    def clean_ingredient(self):
        ingredient = self.cleaned_data.get('ingredient')
        if not ingredient:
            raise forms.ValidationError("This field is required.")
        return ingredient.strip()  # Trim whitespace

class CategoryForm(forms.Form):
    cuisine_type = forms.CharField(label='Cuisine Type', max_length=255)
    meal_type = forms.CharField(label='Meal Type', max_length=255)
    dietary_restrictions = forms.CharField(label='Dietary Restrictions', max_length=255)

    def clean_cuisine_type(self):
        cuisine_type = self.cleaned_data.get('cuisine_type')
        return cuisine_type.strip().lower() if cuisine_type else ""

    def clean_meal_type(self):
        meal_type = self.cleaned_data.get('meal_type')
        return meal_type.strip().lower() if meal_type else ""

    def clean_dietary_restrictions(self):
        dietary_restrictions = self.cleaned_data.get('dietary_restrictions')
        return dietary_restrictions.strip().lower() if dietary_restrictions else ""
