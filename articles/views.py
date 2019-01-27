from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):

    keys = Article.objects.all()
    
    context = {
        'keys' : keys
    }
    return render(request, 'articles/articles.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    
    context = {
        'article': article
    }
    return render(request, 'articles/article.html', context)

def search(request):
    search_list = Article.objects.all()
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            search_list = search_list.filter(Q(title__icontains=keywords) | 
            Q(description__icontains=keywords))
                
    context = {
        'keys' : search_list,
        'values' : request.GET
    }
    return render(request, 'articles/search.html', context)