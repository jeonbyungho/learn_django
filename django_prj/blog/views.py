from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
   model = Post
   template_name = "blog/index.html" # 뷰 파일 지정
   context_object_name = "posts" # 
   ordering = ['-pk']

class PostDetail(DetailView):
   model = Post
   template_name = "blog/detail.html"
   context_object_name = "post"
   pk_url_kwarg = 'post_pk'