from django.db import models
from datetime import datetime
# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    is_mvp = models.BooleanField(default=False)
    hiredDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.author