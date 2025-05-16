from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """投稿フォーム"""
    class Meta:
        model = Post
        fields = ('name', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'あなたの名前'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'メッセージを入力してください', 'rows': 5}),
        } 