from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """投稿フォーム"""
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトルを入力してください'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'メッセージを入力してください', 'rows': 5}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='検索', max_length=100) 