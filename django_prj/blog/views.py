from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

from .models import *
from .forms import *

# 게시판 목록
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

# 게시판 목록 : 카테고리
def category_page(request, slug):
   category = Category.objects.get(slug=slug) if (slug != 'no_category') else None
   return render(request, "blog/index.html", {
      "category"  : category,
      "posts"     : Post.objects.filter(category=category).order_by("-pk"),
      "categorys" : Category.objects.all(),
      "no_category_post_count": Post.objects.filter(category=None).count(),
   })

# 게시판 목록 : 태그
def tag_page(request, slug) -> render:
   tag = Tag.objects.get(slug=slug)
   return render(request, "blog/index.html", {
      "tag"  : tag,
      "posts"     : tag.post_set.all().order_by("-pk"),
      "categorys" : Category.objects.all(),
      "no_category_post_count": Post.objects.filter(category=None).count(),
   })

# 상세 페이지
class PostDetail(DetailView):
   model = Post
   template_name = "blog/detail.html"
   context_object_name = "post"
   pk_url_kwarg = 'post_pk'

   def get_context_data(self, **kwargs):
      context = super(PostDetail, self).get_context_data()
      context['categorys'] = Category.objects.all()
      context['no_category_post_count'] = Post.objects.filter(category=None).count()
      context['comments'] = Comment.objects.filter(post= self.object)
      context['comment_form'] = CommentForm
      return context

# 게시판 작성
class PostCreate(LoginRequiredMixin, CreateView):
   model = Post
   fields = [
   'title', 'hook_text', 'content', 
   'head_image','file_upload', 'category', 
   ]
   
   # 유효성 검사를 통과한 데이터를 처리할 때, 실행되는 로직을 담는다.
   def form_valid(self, form):
      current_user = self.request.user
      if current_user.is_authenticated and current_user.is_staff or current_user.is_superuser:
         form.instance.author = current_user
         result = super(PostCreate, self).form_valid(form)
         
         # 여러 tag 객체 저장 처리
         tags_str = self.request.POST.get('tags_str')
         if tags_str:
            tags_str = tags_str.strip()
            tags_list = tags_str.split(',')

            for t in tags_list:
               t = t.strip()
               tag, is_tag_created = Tag.objects.get_or_create(name=t) # tuple[Tag, bool]
               if is_tag_created:
                  tag.slug = slugify(t, allow_unicode=True)
                  tag.save()
               self.object.tags.add(tag)
               
         return result
      
      return redirect('/blog/')

# 게시판 수정
class PostUpdate(UpdateView):
   model = Post
   fields = [
   'title', 'hook_text', 'content', 
   'head_image','file_upload', 'category', 
   ]
   template_name = 'blog/post_update_form.html'

   def dispatch(self, request, *args: Any, **kwargs: Any):
      current_user = self.request.user
      if current_user.is_authenticated and current_user == self.get_object().author:
         return super(PostUpdate, self).dispatch(request, *args, **kwargs)
      
      return PermissionDenied
   
   def form_valid(self, form):
      response = super(PostUpdate, self).form_valid(form)
      self.object.tags.clear()

      # 여러 tag 객체 저장 처리
      tags_str = self.request.POST.get('tags_str')
      if tags_str:
         tags_str = tags_str.strip()
         tags_list = tags_str.split(',')

         for t in tags_list:
            t = t.strip()
            tag, is_tag_created = Tag.objects.get_or_create(name=t) # tuple[Tag, bool]
            if is_tag_created:
               tag.slug = slugify(t, allow_unicode=True)
               tag.save()
            self.object.tags.add(tag)
      return response

   # HTTP get 요청 시 context 데이터를 처리하는 메서드
   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data()
      if self.object.tags.exists():
         tags_str_list = list()
         for t in self.object.tags.all():
            tags_str_list.append(t.name)
         context['tags_str_default'] = ", ".join(tags_str_list)
      return context

# 게시판에 댓글 추가
def new_comment(request, pk):
   current_user = request.user
   post = Post.objects.get(id=pk)
   if not current_user.is_authenticated:
      return PermissionDenied
   
   if request.method == 'POST':
      # 사용자가 입력한 reqeust를 가지고 CommentForm 인스턴스를 생성한다.
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
         comment = comment_form.save(commit=False)
         comment.post = post
         comment.author = current_user
         comment.save()
         return redirect(comment.get_absolute_url())
   
   return PermissionDenied

# 댓글 수정
class CommontUpdate(LoginRequiredMixin, UpdateView):
   model = Comment
   fields = [
      'content'
   ]

   def dispatch(self, request, *args: Any, **kwargs: Any):
      current_user = self.request.user
      if current_user.is_authenticated and current_user == self.get_object().author:
         return super(CommontUpdate, self).dispatch(request, *args, **kwargs)
      
      return PermissionDenied
   
# 댓글 삭제
def delete_comment(request, pk):
   comment = Comment.objects.get(id=pk)
   if comment == None:
      return Exception
   
   current_user = request.user

   if current_user.is_authenticated and current_user == comment.author:
      post = comment.post
      comment.delete()
      return redirect(post.get_absolute_url())
   
   return PermissionDenied
