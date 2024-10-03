from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Recipe, Ingredient,Category, RecipeIngredient
from django.conf import settings
import json
import os

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name')

from django.forms import formset_factory

fixture_path = os.path.join(settings.BASE_DIR, 'recipe_finder_app', 'fixtures', 'categories.json')
with open(fixture_path) as f:
    categories_data = json.load(f)

for category_data in categories_data:
    Category.objects.get_or_create(name=category_data)

class RecipeForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'instructions','category','image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = forms.CheckboxSelectMultiple()
        self.fields['category'].queryset = Category.objects.all()

class RecipeIngredientForm(forms.ModelForm):
    ingredient_name = forms.CharField()
    quantity = forms.CharField()

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient_name', 'quantity')

    def save(self, commit=True):
        ingredient_name = self.cleaned_data.get('ingredient_name')
        ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
        self.instance.ingredient = ingredient
        self.instance.quantity = self.cleaned_data.get('quantity')

        return super().save(commit)

class RecipeIngredientFormSet(forms.BaseFormSet):
    def __init__(self, *args, **kwargs):
        self.recipe = kwargs.pop('recipe', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instances = super().save(commit=False)
        for instance in instances:
            instance.recipe = self.recipe
            if commit:
                instance.save()
        return instances

RecipeIngredientFormSet = formset_factory(RecipeIngredientForm, extra=1)

from django import forms
# from .models import Category

class RecipeSearchForm(forms.Form):
    ingredients = forms.CharField(label='Ingredients', widget=forms.TextInput(attrs={'placeholder': 'Enter ingredients (separated by commas)'}))
    categories = forms.ModelMultipleChoiceField(label='Categories', queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
