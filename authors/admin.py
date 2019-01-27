from django.contrib import admin
from .models import Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'phone')
    list_display_links = ('id', 'author')
    search_fields = ('author',)
    list_per_page = 25

admin.site.register(Author, AuthorAdmin)