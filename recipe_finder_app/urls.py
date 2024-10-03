# recipe_finder_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_page, name='login_page'),
    path('create_account/', views.create_account, name='create_account'),
    path('home/', views.home_page, name='home_page'),
    path('logout/', views.logout_view, name='logout'),
    path('index/',views.index,name = 'index'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('delete_recipe/<pk>/', views.delete_recipe, name='delete_recipe'),
    path('like_recipe/<int:pk>/', views.like_recipe, name='like_recipe'),
    path('recipe/<int:pk>/', views.recipe_details, name='recipe_details'),
    path('search/', views.search_results, name='search_results'),




    # ... other URL patterns ...
]