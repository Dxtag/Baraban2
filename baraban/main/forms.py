from django import forms
from .models import Post

class PostForm(forms.Form):
    topic =  forms.CharField(max_length=60)
    content = forms.CharField(widget=forms.Textarea)