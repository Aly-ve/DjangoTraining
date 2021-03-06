from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse

from .models import Todo, Comment
from .forms import TodoForm, CommentForm

class IndexView(generic.ListView):
  template_name = 'todo/index.html'
  context_object_name = 'todos'

  def get_queryset(self):
    return Todo.objects.all()
  
  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['form'] = TodoForm()
    return context

class DetailView(generic.DetailView):
  model = Todo
  template_name = 'todo/show.html'

  def get_context_data(self, **kwargs):
    context = super(DetailView, self).get_context_data(**kwargs)
    context['form'] = CommentForm()
    context['comments'] = Comment.objects.filter(task = self.object.id)
    return context

"""
def index(request):
  context = {
    'todos': Todo.objects.all(),
    'form': TodoForm(),
  }
  
  return render(request, 'todo/index.html', context)
  
def show(request, todo_id):
  context = {
    'todo': get_object_or_404(Todo, pk=todo_id),
    'comments': Comment.objects.filter(task=todo_id),
    'form': CommentForm(),
  }
  
  return render(request, 'todo/show.html', context)
"""

def done_todo(request, todo_id):
  if request.method == 'POST':
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.done = True
    todo.save()

  return redirect('/todo')


def new_todo(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      Todo(task=form.cleaned_data['task']).save()
  
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