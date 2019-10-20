from django import forms

class CommentForm(forms.Form):
  comment = forms.CharField(label='Your comment', max_length=512, widget=forms.Textarea)
