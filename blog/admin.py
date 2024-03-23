from django.contrib import admin
from .models import Blog, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "description",
        "is_public",
        "post_date",
    )
    list_display_links = ("title",)
    search_fields = (
        "title",
        "author",
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


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogcommentAdmin)
