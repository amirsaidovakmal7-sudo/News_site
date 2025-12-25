from django.db import models


# Создаем модели

class Category(models.Model):
    category_name = models.TextField(verbose_name="Название категории")
    add_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class News(models.Model):
    title_name = models.CharField(max_length=100, verbose_name='Заголовок')
    news_text = models.TextField('Опишите новость')
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return  self.title_name

# Create your models here.
