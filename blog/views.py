from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article

class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
