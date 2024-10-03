from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUserManager(models.Manager):
    pass  # You can add custom manager methods here if needed

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default = "No description available")
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', related_name='recipes')
    instructions = models.TextField(default="No instructions available")
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipe_images',default='recipe_images/chai.jpeg')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_recipes')

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.name} - {self.quantity}"
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)