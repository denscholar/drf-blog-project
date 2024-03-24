from .models import Blog
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import BlogSerializer
from django.shortcuts import render, get_object_or_404, redirect


# class-based views
class Blog_list_APIView(APIView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(blogs, many=True)
        response = {
                "data": serializer.data
            }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(data=blogs)
        if serializer.is_valid():
            serializer.save()
            response = {
                "data": "data created successfully"
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response({'status': "data not valid"}, status=status.HTTP_400_BAD_REQUEST)


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
        return Response({'status': "data not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
    # delete data  
    def delete(self, request, id):
         blog = get_object_or_404(Blog, id=id)
         serializer = BlogSerializer(blog)
         serializer.delete()
         return Response({'status': "data deleted successfully"}, status=status.HTTP_200_OK)

        
    

        

# @api_view(["GET", "POST"])
# def blog_list(request):
#     if request.method == "GET":
#         blogs = Blog.objects.filter(is_public=True)
#         serializers = BlogSerializer(blogs, many=True)
#         response = {
#             "blogs": serializers.data,
#         }
#         return Response(data=response, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         data = request.data
#         serializer = BlogSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "post successfully created"}
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(["GET", "PUT", "DELETE"])
# def blog_update(request, id):
#     if  request.method == "GET":
#         blogs = Blog.objects.get(id=id)
#         serializer = BlogSerializer(blogs)
#         response = {
#             "blog": serializer.data,
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
    

#     if request.method == "PUT":
#         # get a single blog
#         blog = Blog.objects.get(id=id)
#         # note, when updating, you need to pass the insstance
#         serializer = BlogSerializer(data=request.data, instance=blog)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': "data updated successfully"}, status=status.HTTP_200_OK)
#         return Response({'status': "data not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#          # get a single blog
#         blog = Blog.objects.get(id=id)
#         blog.delete()
#         return Response({'status': "data deleted successfully"}, status=status.HTTP_200_OK)
#     return Response({'status': "data not valid"}, status=status.HTTP_400_BAD_REQUEST)


    