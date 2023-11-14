from django.urls import path
from . import views

urlpatterns = [
   path("", views.PostList.as_view(), name='blog'),
   path("<int:post_pk>/", views.PostDetail.as_view(), name='detail'),
   path("category/<str:slug>", views.category_page),
]