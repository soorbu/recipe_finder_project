from django.contrib import admin
from .models import User, Recipe, Ingredient, Category

# Register the User model with a custom UserAdmin class
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'userid')  # Display userid in the list view
    readonly_fields = ('userid',)  # Make userid read-only

admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
