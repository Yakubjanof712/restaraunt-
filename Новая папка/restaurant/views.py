from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish
from .forms import CategoryForm, DishForm

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant/dish_list.html', {'dishes': dishes})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    return render(request, 'restaurant/dish_detail.html', {'dish': dish})

def dishes_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    dishes = Dish.objects.filter(category=category)
    return render(request, 'restaurant/dishes_by_category.html', {'category': category, 'dishes': dishes})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = CategoryForm()
    return render(request, 'restaurant/category_form.html', {'form': form})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'restaurant/dish_form.html', {'form': form})

def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'restaurant/category_form.html', {'form': form})


def dish_update(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'restaurant/dish_form.html', {'form': form})


def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('dish_list')
    return render(request, 'restaurant/category_confirm_delete.html', {'category': category})

def dish_delete(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'restaurant/dish_confirm_delete.html', {'dish': dish})
