from django.db import models
from django.utils import timezone

class Post(models.Model):
    """掲示板の投稿モデル"""
    title = models.CharField(max_length=200, default='未設定')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "投稿"
        verbose_name_plural = "投稿一覧"

    @classmethod
    def search(cls, query):
        return cls.objects.filter(models.Q(title__icontains=query) | models.Q(content__icontains=query))
