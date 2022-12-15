from articles import models
from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(upload_to='pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('home', kwargs={'pk': self.pk})
