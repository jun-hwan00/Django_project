from django.shortcuts import render
# C:\Users\user\Django_project\mysite\api\views.py
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post # blog 앱의 Post 모델 임포트

# Post 객체 목록 조회 및 생성 API View
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.
