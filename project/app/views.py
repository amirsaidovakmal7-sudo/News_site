from django.shortcuts import render
from .models import Category, News

def home_page(request):
    # Достаем данные из бд
    categories = Category.objects.all()
    news = News.objects.all()
    # Передаем данные на фронт
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'home.html', context)

def category_page(request, pk):
    category = Category.objects.get(pk=pk)
    news = News.objects.filter(news_category=category)
    context = {
        'category': category,
        'new': news
    }
    return render(request, 'category.html', context)


def news_page(request, pk):
    new = News.objects.get(id=pk)
    context = {
        'new': new
    }
    return render(request, 'news.html', context)



# Create your views here.
