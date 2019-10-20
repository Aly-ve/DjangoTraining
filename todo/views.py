from django.shortcuts import render, get_object_or_404, redirect

from .models import Todo, Comment
from .forms import CommentForm

def index(request):
  context = {
    'todos': Todo.objects.all(),
  }
  
  return render(request, 'todo/index.html', context)
  
def show(request, todo_id):
  context = {
    'todo': get_object_or_404(Todo, pk=todo_id),
    'comments': Comment.objects.filter(task=todo_id),
    'form': CommentForm(),
  }
  
  return render(request, 'todo/show.html', context)

def done_todo(request, todo_id):
  if request.method == 'POST':
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.done = True
    todo.save()

  return redirect('/todo')

def new_comment(request, todo_id):
  if request.method == 'POST':
    todo = get_object_or_404(Todo, pk=todo_id)
    form = CommentForm(request.POST)
    if form.is_valid():
      Comment(comment=form.cleaned_data['comment'], task=todo).save()
      
      return redirect('/todo/{}/'.format(todo_id,))
  else:
    return redirect('/todo')