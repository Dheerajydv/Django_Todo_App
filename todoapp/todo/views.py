from django.shortcuts import render


# Create your views here.
def all_todos(request):
    return render(request ,'todos.html')