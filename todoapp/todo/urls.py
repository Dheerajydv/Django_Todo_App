from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos, name='all_todos'),
    path('add', views.add_todo, name='add_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
    path('register/', views.register, name='register'),
]
