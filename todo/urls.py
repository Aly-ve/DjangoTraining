from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('add', views.new_todo, name='new_todo'),
  path('<int:todo_id>/add', views.new_comment, name='new_comment'),
  path('<int:todo_id>/done', views.done_todo, name='done_todo'),
]