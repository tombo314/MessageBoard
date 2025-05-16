from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm, SearchForm

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
        title = request.POST.get('title')
        content = request.POST.get('content')

        # デバッグ用の出力
        print(f"Title: {title}, Content: {content}")

        # Postモデルのインスタンスを作成して保存
        post = Post(title=title, content=content)
        post.save()
        
        print("Post saved successfully!")  # 保存成功のメッセージ
        
        return redirect('board:index')
    
    return redirect('board:index')

def search(request):
    query = request.GET.get('q')  # クエリパラメータから検索文字列を取得
    results = Post.objects.filter(content__icontains=query) if query else []  # 検索結果を取得
    return render(request, 'board/search_results.html', {'results': results, 'query': query})

def search_posts(request):
    form = SearchForm()
    results = []
    
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(content__icontains=query)  # 投稿の内容にクエリが含まれるものを検索

    return render(request, 'search_results.html', {'form': form, 'results': results})
