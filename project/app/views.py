from django.shortcuts import render, redirect
from .models import Category, News
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View
from . import forms


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
    news = News.objects.get(id=pk)
    context = {
        'new': news
    }
    return render(request, 'news.html', context)

def search(request):
    if request.method == 'POST':
        search_news = request.POST.get('search-news')
        get_news = News.objects.filter(title_name__icontains=search_news)
        context = {}
        if get_news:
            context.update(user_news=search_news, news=get_news)
        else:
            context.update(user_news=search_news, news='')
        return render(request, 'result.html', context)


# Делаем регестрацию

class Registration(View):
    template_name = 'registration/register.html'
    def get(self, request):
        form = forms.RegisterForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)

            user.save()
            login(request, user)
        return redirect('/')


def logout_page(request):
    logout(request)
    return redirect('/')




# Create your views here.
