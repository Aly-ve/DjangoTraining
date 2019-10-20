from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:todo_id>/', views.show, name='show'),
  path('<int:todo_id>/add', views.new_comment, name='new_comment'),
  path('<int:todo_id>/done', views.done_todo, name='done_todo'),
]