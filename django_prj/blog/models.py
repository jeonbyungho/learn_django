from django.db import models

class Post(models.Model):
   # 제목
   title = models.CharField(max_length=50)

   # 내용
   content = models.TextField()

   # 작성일 auto_now_add : 필드가 생성될 때 자동으로 값이 할당된다.
   created_at = models.DateTimeField(auto_now_add=True)

   # 수정 날짜 auto_now : 필드가 저장될 때 항상 현재 시간으로 자동으로 할당된다.
   updated_at = models.DateTimeField(auto_now=True)
   
   # 작성자
   author = models.TextField()

   def __str__(self):
      return f'[{self.pk}] {self.title}'
   
   # get_absolute_url(self) : 관리자 페이지에서 site view 버튼이 생성됨
   # 모델의 인스턴스를 대표하는 url를 반환한다.
   def get_absolute_url(self):
      return f'/blog/{self.pk}/'