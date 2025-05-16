from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm

# Create your views here.

class IndexView(generic.ListView):
    """掲示板一覧表示"""
    model = Post
    template_name = 'board/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context
    
def post_create(request):
    """新規投稿"""
    if request.method == 'POST':
        # フォームからデータを取得して保存
        name = request.POST.get('username')
        message = request.POST.get('content')
        
        # Postモデルのインスタンスを作成して保存
        post = Post(name=name, message=message)
        post.save()
        
        return redirect('board:index')
    
    return redirect('board:index')
