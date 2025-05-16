from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.post_create, name='post_create'),
] 