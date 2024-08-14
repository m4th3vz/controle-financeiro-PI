# staticpages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL para página de boas-vindas
    path('', views.welcome, name='welcome'),
    # URL para a página sobre
    path('about/', views.about, name='about'),
    # URL para a página de notícias
    path('news/', views.news, name='news'),
    # URL para a página de notícia 1
    path('news1/', views.news1, name='news1'),
    # URL para a página de notícia 2
    path('news2/', views.news2, name='news2'),
]
