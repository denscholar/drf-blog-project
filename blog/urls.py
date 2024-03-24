from django.urls import path
from . import views
from .views import Blog_list_APIView


urlpatterns = [
   # path("", views.blog_list, name='blog-list'),
   # path("updated/<int:id>/", views.blog_update, name='blog-update'),
   path("", Blog_list_APIView.as_view(), name='blog-list'),
]
