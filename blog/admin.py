from django.contrib import admin
from .models import Blog, BlogComment, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "blog_title",
        "category",
        "blog_author",
        "blog_description",
        "is_public",
        "post_date",
    )
    list_display_links = ("blog_title",)
    search_fields = (
        "blog_title",
        "blog_author",
    )
    list_per_page = 5
    list_editable = ("is_public",)


class BlogcommentAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "author",
        "comment_date",
    )
    list_display_links = ("description",)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogcommentAdmin)

