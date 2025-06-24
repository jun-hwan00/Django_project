# C:\Users\user\Django_project\mysite\api\urls.py
from django.urls import path
from . import views # api 앱의 views 임포트

urlpatterns = [
    path('Post/', views.PostListCreate.as_view(), name='post-list-create'),
]