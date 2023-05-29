# Django不同版本的urls.py文件的写法不同，这里使用的是Django 2.0的写法
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]