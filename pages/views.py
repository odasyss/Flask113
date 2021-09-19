from django.views.generic import TemplateView
from articles.models import Article


class HomePageView(TemplateView):
    model = Article
    template_name = 'home.html'



