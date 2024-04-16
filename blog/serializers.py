from rest_framework import serializers
from blog.models import Blog, Category


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
    # string related
    # category = serializers.StringRelatedField(many=True)

    # primary key related field
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # nestted serializer
    category_name = serializers.CharField()

    category = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="category_detail",
    )


    # category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'category']
        # exclude = ("id",)
