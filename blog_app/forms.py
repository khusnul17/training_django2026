from django import forms
from .models import Blogs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'content', 'created_by', 'created_at']
        widgets = {'created_at': forms.DateTimeInput(attrs={'type':'datetime-local'})}