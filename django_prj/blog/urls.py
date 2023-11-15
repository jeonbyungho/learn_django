from django.urls import path
from . import views

urlpatterns = [
   path("", views.PostList.as_view(), name='blog'),
   path("<int:post_pk>/", views.PostDetail.as_view(), name='detail'),
   path("category/<str:slug>", views.category_page),
   path("tag/<str:slug>", views.tag_page),
   path("create_post/",views.PostCreate.as_view(), name="create_post"),
   path("update_post/<int:pk>/",views.PostUpdate.as_view(), name="update_post"),
]