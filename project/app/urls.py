from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('new/<int:pk>', views.news_page),

]