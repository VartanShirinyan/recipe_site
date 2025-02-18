from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.apps import apps


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# class Recipe(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     cooking_stages = models.TextField(verbose_name='Этапы приготовления')
#     cooking_hours = models.PositiveIntegerField(default=0, verbose_name='Часы приготовления')  # Новое поле
#     cooking_minutes = models.PositiveIntegerField(default=0, verbose_name='Минуты приготовления')  # Новое поле
#     image = models.ImageField(upload_to='recipes/images/', verbose_name='Изображение')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

#     def __str__(self):
#         return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_stages = models.TextField()
    cooking_hours = models.PositiveIntegerField(default=0)
    cooking_minutes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='recipes/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_stages', 'cooking_hours', 'cooking_minutes', 'image', 'author', 'category']  # Новые поля
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'cooking_stages': 'Этапы приготовления',
            'cooking_hours': 'Часы приготовления',
            'cooking_minutes': 'Минуты приготовления',
            'image': 'Изображение',
            'category': 'Категория',
            'author': 'Автор',
        }

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("Это поле обязательно.")
        return category

 