from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Recipe, Category
from .forms import RecipeForm


# Create your views here.
def home(request):
    recipes = Recipe.objects.all()[:5]  # Получаем 5 случайных рецептов
    return render(request, 'recipes/home.html', {'recipes': recipes})

# def recipe_list(request):
#     recipes = Recipe.objects.all()  # Получение всех рецептов из базы данных
#     return render(request, 'recipes/recipe_list.html', {'recipes': recipes})  # Передача списка рецептов в шаблон

def recipe_list(request):
    category_id = request.GET.get('category')
    if category_id:
        recipes = Recipe.objects.filter(category_id=category_id)
    else:
        recipes = Recipe.objects.all()
    categories = Category.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'categories': categories})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        print(request.POST)
        form = RecipeForm(request.POST, request.FILES)  # Считывание данных формы
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Если имя не указано, устанавливаем 'Аноним'
            recipe.category_id = request.POST.get('category')
            recipe.save()
            return redirect('recipe_list')
        else:
            print(form.errors)  # Дополнительная отладка
            print("Form data:", request.POST)  # Печать данных формы для анализа
    else:
        form = RecipeForm()
    
    categories = Category.objects.all()
    return render(request, 'recipes/add_recipe.html', {'form': form, 'categories': categories})

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Проверяем, что текущий пользователь является автором рецепта
    if recipe.author == request.user:
        recipe.delete()
    
    return redirect('recipe_list')  # Перенаправляем на список рецептов после удаления

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} успешно создан! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

@login_required
# def edit_recipe(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
    
#     # Проверяем, что текущий пользователь является автором рецепта
#     if recipe.author != request.user:
#         return redirect('recipe_list')
    
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_detail', pk=recipe.pk)
#     else:
#         form = RecipeForm(instance=recipe)
    
#     categories = Category.objects.all()
#     return render(request, 'recipes/edit_recipe.html', {'form': form, 'categories': categories})

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(instance=recipe)
    categories = Category.objects.all()
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'categories': categories})