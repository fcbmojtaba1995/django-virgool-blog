from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'reading_time', 'status')
        widgets = {
            'reading_time': forms.NumberInput(attrs={'placeholder': "enter to minutes"})
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'reading_time', 'status')