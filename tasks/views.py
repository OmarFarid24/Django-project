from django.shortcuts import render
from .models import ToDoList


def dashboard(request):
    lists = ToDoList.objects.all()

    context = {
        'lists': lists
    }

    return render(request, 'tasks/dashboard.html', context)
