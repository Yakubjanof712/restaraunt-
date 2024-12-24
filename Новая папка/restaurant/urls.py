from django.urls import path
from . import views

urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('category/<int:category_id>/dishes/', views.dishes_by_category, name='dishes_by_category'),
    path('category/create/', views.category_create, name='category_create'),
    path('dish/create/', views.dish_create, name='dish_create'),
    path('category/<int:category_id>/update/', views.category_update, name='category_update'),
    path('dish/<int:dish_id>/update/', views.dish_update, name='dish_update'),
    path('category/<int:category_id>/delete/', views.category_delete, name='category_delete'),
    path('dish/<int:dish_id>/delete/', views.dish_delete, name='dish_delete'),

]




