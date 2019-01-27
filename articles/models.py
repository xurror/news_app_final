from django.db import models
from datetime import datetime
from authors.models import Author
# Create your models here.

class Article(models.Model):
    # Constants in Model class
    COURSES = 'COURSES'
    FINANCE = 'FINANCE'
    TECHNOLOGY = 'TECHNOLOGY'
    BUSINESS = 'BUSINESS'
    categories = (
        (COURSES, 'courses'),
        (FINANCE, 'finance'),
        (TECHNOLOGY, 'technology'),
        (BUSINESS, 'business'),
    )
    
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=100, default=COURSES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True)
    publishedAt = models.DateTimeField(default=datetime.now, blank=True)
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.title

