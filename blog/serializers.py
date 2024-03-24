from rest_framework import serializers

from blog.models import Blog


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
