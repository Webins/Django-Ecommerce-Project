from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # when a category is deleted all the products attached to it will be deleted   
    created_date = models.DateTimeField(auto_now_add=True) # auto_now_add is used when is created for the first time
    modified_date = models.DateTimeField(auto_now=True) # auto_now is used when the object could change its date


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug]) # reverse trae la URL original del producto

    def __str__(self):
        return self.name
