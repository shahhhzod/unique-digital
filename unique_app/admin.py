from django.contrib import admin
from .models import Post, Category, PortfolioItem

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'views', 'image')  # Убедитесь, что все эти атрибуты существуют в модели `Post`

# Зарегистрируем модель Category обычным способом
admin.site.register(Category)
admin.site.register(PortfolioItem)
