from django.contrib import admin
from django.urls import path
from .views import all_todos

urlpatterns = [
    path('', all_todos, name='all_todos'),
]
