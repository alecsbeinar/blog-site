from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=250)
    full_text = models.TextField()
    summary = models.TextField()
    category = models.CharField(max_length=250)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=250, unique=True)
    og_image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f'Заголовок: {self.title} | Категория: {self.category}'

    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug': self.slug})

    def get_category_url(self):
        return reverse('category_page', kwargs={'category': self.category})
