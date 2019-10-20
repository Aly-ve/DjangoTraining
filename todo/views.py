from django.shortcuts import render, get_object_or_404, redirect

from .models import Todo, Comment
from .forms import TodoForm, CommentForm

def index(request):
  context = {
    'todos': Todo.objects.all(),
    'form': TodoForm(),
  }
  
  return render(request, 'todo/index.html', context)
