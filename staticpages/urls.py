# staticpages/urls.py
from django.urls import path
from .views import WelcomeView, AboutView, NewsView, News1View, News2View

urlpatterns = [
    # URL para página de boas-vindas
    path('', WelcomeView.as_view(), name='welcome'),
    # URL para a página sobre
    path('about/', AboutView.as_view(), name='about'),
    # URL para a página de notícias
    path('news/', NewsView.as_view(), name='news'),
    # URL para a página de notícia 1
    path('news1/', News1View.as_view(), name='news1'),
    # URL para a página de notícia 2
    path('news2/', News2View.as_view(), name='news2'),
]
