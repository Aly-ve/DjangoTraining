from django.shortcuts import render, get_object_or_404, redirect

from .models import Todo

def index(request):
  context = {
    'todos': Todo.objects.all(),
  }
  
  return render(request, 'todo/index.html', context)
