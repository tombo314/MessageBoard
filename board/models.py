from django.db import models
from django.utils import timezone

class Post(models.Model):
    """掲示板の投稿モデル"""
    name = models.CharField("投稿者名", max_length=100)
    message = models.TextField("メッセージ")
    created_at = models.DateTimeField("投稿日時", default=timezone.now)

    def __str__(self):
        return f"{self.name}: {self.message[:20]}"
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "投稿"
        verbose_name_plural = "投稿一覧"
