from django.urls import path
from . import views

urlpatterns = [
   path("", views.PostList.as_view(), name='blog'), # path("", views.index, name='blog'),
   path("<int:post_pk>/", views.detail_post, name='detail'),
]