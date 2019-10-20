from django import forms

class TodoForm(forms.Form):
  task = forms.CharField(label='Your task', max_length=140)

class CommentForm(forms.Form):
  comment = forms.CharField(label='Your comment', max_length=512, widget=forms.Textarea)
