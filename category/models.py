from django.db import models
from django.urls import reverse, NoReverseMatch
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta():
        # this is to fix the correct plural for some words (when default it just add an S)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug]) # reverse  refer to the URL only by its name attribute

    def __str__(self):
        return self.name


