from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Recipe(models.Model):
    recipeid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(default="No description available")
    instructions = models.TextField(default="No instructions available")
    imageurl = models.ImageField(upload_to='images/', default='path/to/default_image.jpg')
    userid = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipeid = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # Foreign key to Recipe
    ingredient = models.CharField(max_length=255)


    def __str__(self):
        return self.ingredient

class Category(models.Model):
    recipeid = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # Foreign key to Recipe
    cuisine_type = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=255)
    dietary_restrictions = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cuisine_type}, {self.meal_type}, {self.dietary_restrictions}"
