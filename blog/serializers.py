from rest_framework import serializers
from blog.models import Blog, Category, WeeklySchedule


class BlogSerializer(serializers.ModelSerializer):
    len_blog_title = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            "blog_title",
            "blog_author",
            "category",
            "blog_description",
            "len_blog_title",
            "is_public",
        )

    def get_len_blog_title(self, object):
        return len(object.blog_title)


class CategorySerializer(serializers.ModelSerializer):
    # nestted serializer
    category_name = serializers.CharField() 
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        exclude = ("id",)
