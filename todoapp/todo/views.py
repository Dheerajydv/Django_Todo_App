from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from .forms import TodoForm, UserRegisterationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.http import JsonResponse

# Create your views here.

def all_todos(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request ,'todos.html', {'todos': todos,})

@login_required
def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('all_todos')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('all_todos')
    return render(request, 'delete_todo.html', {'todo': todo})

@login_required
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect('all_todos')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_todos')
    else:
        form = UserRegisterationForm()
    return render(request, 'registration/register.html', {'form': form})