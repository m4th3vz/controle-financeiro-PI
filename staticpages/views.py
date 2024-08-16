# staticpages/views.py
from django.views.generic import TemplateView

# Página de boas-vindas
class WelcomeView(TemplateView):
    template_name = 'staticpages/welcome.html'

# Página de sobre
class AboutView(TemplateView):
    template_name = 'staticpages/about.html'

# Página de notícias
class NewsView(TemplateView):
    template_name = 'staticpages/news.html'

# Página de notícia 1
class News1View(TemplateView):
    template_name = 'staticpages/news1.html'

# Página de notícia 2
class News2View(TemplateView):
    template_name = 'staticpages/news2.html'
