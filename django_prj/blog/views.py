from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# def index(request):
#    posts = Post.objects.all().order_by('-pk')
#    return render(request, "blog/index.html", {"posts": posts})

class PostList(ListView):
   model = Post
   template_name = "blog/index.html" # 뷰 파일 지정
   context_object_name = "posts" # 
   ordering = ['-pk']


def detail_post(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   return render(request, "blog/detail.html", {"post": post})