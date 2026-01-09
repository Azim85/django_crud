from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "image"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border rounded-lg"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border rounded-lg",
                "rows": 5
            }),
        }
