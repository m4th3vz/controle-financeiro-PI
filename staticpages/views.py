# staticpages/views.py
from django.shortcuts import render

# Página de boas-vindas
def welcome(request):
    return render(request, 'staticpages/welcome.html')

# Página de sobre
def about(request):
    return render(request, 'staticpages/about.html')

# Página de notícias
def news(request):
    return render(request, 'staticpages/news.html')

# Página de notícia 1
def news1(request):
    return render(request, 'staticpages/news1.html')

# Página de notícia 2
def news2(request):
    return render(request, 'staticpages/news2.html')
