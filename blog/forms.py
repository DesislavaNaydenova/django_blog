from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        form = ('body',)
        fields = ['body', ]  # List all fields you want in the form