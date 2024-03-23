from django.urls import path
from . import views


urlpatterns = [
   path("", views.blog_list, name='blog-list'),
   path("updated/<int:id>/", views.blog_update, name='blog-update')
]
