from django.db import models

class Todo(models.Model):
  task = models.CharField(max_length=140)
  done = models.BooleanField(default=False)
  created_at = models.DateTimeField('created_at', auto_now_add=True)
  updated_at = models.DateTimeField('updated_at', auto_now=True)
