from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("<int:post_pk>/", views.detail_post, name='detail'),
]