# from django.contrib import admin
# from .models import Category, Recipe, Ingredient, RecipeIngredient,Like, CustomUser

# admin.site.register(Category)
# admin.site.register(Recipe)
# admin.site.register(Ingredient)
# admin.site.register(RecipeIngredient)
# admin.site.register(Like)
# admin.site.register(CustomUser)

from django.contrib import admin
from .models import CustomUser, Recipe, Ingredient, Category

# Register all models to be visible in the Django Admin interface
admin.site.register(CustomUser)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
