from django.shortcuts import render
from articles.models import Article
from authors.models import Author
# Create your views here.

def index(request):

    keys = Article.objects.order_by('-publishedAt')

    context = {
        'keys': keys,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    #Get all reporters
    authors = Author.objects.order_by('-author')

    #Get MVP
    #mvp_reporter = Author.objects.all().filter(is_mvp=True)

    context = {
        'authors' : authors,        
    }
    return render(request, 'pages/about.html', context)
