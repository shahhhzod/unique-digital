from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

# Сначала определяем класс Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# Затем определяем класс Post, который ссылается на Category
class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)  # Или models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    categories = models.ManyToManyField('Category', related_name='posts')  # Использование строки для ссылки на модель

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    project_type = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='inquiries/', blank=True, null=True)

    def __str__(self):
        return f"Inquiry from {self.full_name}"
    

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
