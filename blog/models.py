from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True)
    blog_description = models.TextField()
    post_date = models.DateField(default=timezone.now)
    is_public = models.BooleanField(default=False)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.blog_title + " ==> " + str(self.blog_author)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title + "-" + str(self.post_date))
        return super().save(*args, **kwargs)


class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog
    

