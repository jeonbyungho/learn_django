from typing import Any
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

class PostList(ListView):
   model = Post
   template_name = "blog/index.html" # 뷰 파일 지정
   context_object_name = "posts" # 
   ordering = ['-pk']

   def get_context_data(self, **kwargs):
      # super 부모 클래스의 get_context_data()를 호출한다.
      context = super(PostList, self).get_context_data()
      context['categorys'] = Category.objects.all()
      context['no_category_post_count'] = Post.objects.filter(category=None).count()
      return context

class PostDetail(DetailView):
   model = Post
   template_name = "blog/detail.html"
   context_object_name = "post"
   pk_url_kwarg = 'post_pk'