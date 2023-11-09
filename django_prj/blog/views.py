from django.shortcuts import render
from .models import Post

def index(request):
   posts = Post.objects.all().order_by('-pk')
   return render(request, "blog/index.html", {"posts": posts})

def detail_post(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   return render(request, "blog/detail.html", {"post": post})