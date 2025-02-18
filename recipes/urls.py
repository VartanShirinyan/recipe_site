# recipes/urls.py
# from django.urls import path
# from .views import home, recipe_list, recipe_detail, add_recipe

# urlpatterns = [
#     path('', home, name='home'),
#     path('recipes/', recipe_list, name='recipe_list'),
#     path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
#     path('add-recipe/', add_recipe, name='add_recipe'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('recipes/', views.recipe_list, name='recipe_list'),
#     path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
#     path('add-recipe/', views.add_recipe, name='add_recipe'),
#     path('recipes/delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),  # Новый маршрут для удаления
# ]

from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('recipes/', views.recipe_list, name='recipe_list'),
#     path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
#     path('add-recipe/', views.add_recipe, name='add_recipe'),
#     path('recipes/delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),

#     # Маршруты для аутентификации
#     path('register/', views.register, name='register'),  # Регистрация
#     path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),  # Вход
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Выход
# ]

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('recipes/delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('recipes/edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),

    # Маршруты для аутентификации
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),  # Вход
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Выход
]