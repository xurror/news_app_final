from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publishedAt')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('author', 'title',)
    list_per_page = 25

admin.site.register(Article, ArticleAdmin)