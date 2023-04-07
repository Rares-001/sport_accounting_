from django.db import models
from django.urls import reverse

# Create your models here.

def get_url():
    return reverse('products_by_category')


class Category(models.Model):
    bar_category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    drink_description = models.TextField(max_length=255, blank=True)
    drink_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.bar_category_name
