from django.urls import path
from .views import Blog_list_APIView, Category_detailAPIView, Category_listApiView


urlpatterns = [
    # path("", views.blog_list, name='blog-list'),
    # path("updated/<int:id>/", views.blog_update, name='blog-update'),
    path("", Blog_list_APIView.as_view(), name="blog-list"),
    # category
    path("category_list/", Category_listApiView.as_view(), name="category_list"),
    path("category_detail/<int:pk>/", Category_detailAPIView.as_view(), name="category_detail"),
]
