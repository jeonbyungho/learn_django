from django.db import models

class Post(models.Model):
   # 제목
   title = models.CharField(max_length=50)
   # 내용
   content = models.TextField()
   # 작성일
   create_at = models.DateTimeField()
   # 작성자
   # author

   def __str__(self):
      return f'[{self.pk} {self.title}]'