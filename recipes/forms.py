# from django import forms
# from .models import Recipe

# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['title', 'description', 'cooking_stages', 'cooking_hours', 'cooking_minutes', 'image', 'category']
#         labels = {
#             'title': 'Название',
#             'description': 'Описание',
#             'cooking_stages': 'Этапы приготовления',
#             'cooking_hours': 'Часы приготовления',
#             'cooking_minutes': 'Минуты приготовления',
#             'image': 'Изображение',
#             'category': 'Категория',
#         }
#         widgets = {
#             'category': forms.Select(attrs={'class': 'form-control'}),
#         }

from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_stages', 'cooking_hours', 'cooking_minutes', 'image', 'category']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'cooking_stages': 'Этапы приготовления',
            'cooking_hours': 'Часы приготовления',
            'cooking_minutes': 'Минуты приготовления',
            'image': 'Изображение',
            'category': 'Категория',
        }

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("Это поле обязательно.")
        return category