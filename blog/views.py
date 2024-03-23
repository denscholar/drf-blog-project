# from django.http import JsonResponse
from .models import Blog
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BlogSerializer


@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(is_public=True)
        serializers = BlogSerializer(blogs, many=True)
        response = {
            "blogs": serializers.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    if request.method == "POST":
        data = request.data
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "post successfully created"}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE"])
def blog_update(request, id):
    if  request.method == "GET":
        blogs = Blog.objects.get(id=id)
        serializer = BlogSerializer(blogs)
        response = {
            "blog": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)
    

    if request.method == "PUT":
        # get a single blog
        blog = Blog.objects.get(id=id)
        # note, when updating, you need to pass the insstance
        serializer = BlogSerializer(data=request.data, instance=blog)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': "data updated successfully"}, status=status.HTTP_200_OK)
        return Response({'status': "data not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
         # get a single blog
        blog = Blog.objects.get(id=id)
        blog.delete()
        return Response({'status': "data deleted successfully"}, status=status.HTTP_200_OK)
    return Response({'status': "data not valid"}, status=status.HTTP_400_BAD_REQUEST)


    