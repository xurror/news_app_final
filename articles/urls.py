from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles'),
    path('<int:article_id>', views.article, name='article'),
    path('search', views.search, name='search'),
]
