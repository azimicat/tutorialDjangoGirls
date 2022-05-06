from django import forms
from .models import Post as Post_sv


class PostForm(forms.ModelForm):
    class Meta:
        model = Post_sv
        fields = ('title', 'text',)
