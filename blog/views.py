from .models import Blog, Category, WeeklySchedule
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import BlogSerializer, CategorySerializer, ScheduleSerializer
from django.shortcuts import render, get_object_or_404, redirect


# class-based views
class Blog_list_APIView(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(blogs, many=True)
        response = {"data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(data=blogs)
        if serializer.is_valid():
            serializer.save()
            response = {"data": "data created successfully"}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(
            {"status": "data not valid"}, status=status.HTTP_400_BAD_REQUEST
        )


class Blog_detail(APIView):
    # get blog details
    def get(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        serializer = BlogSerializer(blog)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # update product
    def put(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        serializer = BlogSerializer(data=blog, instance=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"status": "data not valid"}, status=status.HTTP_400_BAD_REQUEST
        )

    # delete data
    def delete(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        serializer = BlogSerializer(blog)
        serializer.delete()
        return Response(
            {"status": "data deleted successfully"}, status=status.HTTP_200_OK
        )


class Category_listApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


class Category_detailAPIView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


