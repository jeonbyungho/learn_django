from django.db import models
from django.contrib.auth.models import User
import os

# 카테고리
class Category(models.Model):
   name = models.CharField(max_length=50, unique=True)
   # allow_unicode : 한글을 포함한 모든 유니코드 문자를 지원해준다.
   slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return f'/blog/category/{self.slug}'

   class Meta:
      # verbose_name_plural : 관리자 페이지에서 보여질 모델명을 지정한다.
      verbose_name_plural = 'Categories'

# 태그
class Tag(models.Model):
   name = models.CharField(max_length=50, unique=True)
   slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return f'/blog/tag/{self.slug}'

   class Meta:
      verbose_name_plural = 'Tags'

# 게시판
class Post(models.Model):
   # 제목
   title = models.CharField(max_length=50)

   # 요약문
   hook_text = models.CharField(max_length=100, blank=True)

   # 내용
   content = models.TextField()

   # 작성일 auto_now_add : 필드가 생성될 때 자동으로 값이 할당된다.
   created_at = models.DateTimeField(auto_now_add=True)

   # 수정 날짜 auto_now : 필드가 저장될 때 항상 현재 시간으로 자동으로 할당된다.
   updated_at = models.DateTimeField(auto_now=True)
   
   # 작성자
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

   # 카테고리
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

   # 대표 이미지 upload_to : 저장될 경로와 이름 양식을 지정, blank : 빈 값 허용 여부
   head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)

   # 파일
   file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d', blank=True)

   # 태그 N:N 관계
   tags = models.ManyToManyField(Tag, blank=True)
   
   def __str__(self):
      return f'[{self.pk}] {self.title} :: {self.author}'
   
   # get_absolute_url(self) : 관리자 페이지에서 site view 버튼이 생성됨
   # 모델의 인스턴스를 대표하는 url를 반환한다.
   def get_absolute_url(self):
      return f'/blog/{self.pk}/'
   
   # os.path.basename() : 주어진 경로 문자열에서 파일또는 디렉토리의 기본 이름을 추출하는 함수, 즉 파일 시스템에서 마지막 요소를 반환한다.
   def get_file_name(self):
      return os.path.basename(self.file_upload.name)
   
   def get_file_ext(self):
      return self.get_file_name()[1]