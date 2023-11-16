from django.urls import path
from . import views

urlpatterns = [
   path("", views.PostList.as_view(), name='blog'),
   path("<int:post_pk>/", views.PostDetail.as_view(), name='detail'),

   path("category/<str:slug>", views.category_page),
   path("tag/<str:slug>", views.tag_page),
   path("search/<str:q>/",views.PostSearch.as_view(), name="search_post"),

   path("create_post/",views.PostCreate.as_view(), name="create_post"),
   path("update_post/<int:pk>/",views.PostUpdate.as_view(), name="update_post"),

   path("<int:pk>/new_comment/",views.new_comment, name="new_comment"),
   path("update_comment/<int:pk>/",views.CommontUpdate.as_view(), name="update_comment"),
   path("delete_comment/<int:pk>/",views.delete_comment, name="delete_comment"),
]