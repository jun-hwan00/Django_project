# C:\Users\user\Django_project\mysite\api\serializers.py
from rest_framework import serializers
from blog.models import Post # blog 앱의 Post 모델 임포트

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # 안드로이드 앱에서 보내는 필드와 일치하도록 설정
        fields = ['id', 'author', 'title', 'text', 'created_date', 'published_date']
        # 이미지 필드가 있다면 'image'도 추가
        # fields = ['id', 'author', 'title', 'text', 'created_date', 'published_date', 'image']