from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    A blog post.

    Related:
        :model:`auth.User`.
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField("image", default="placeholder")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A blog post comment.

    Related:
        :model:`auth.User`
        :model:`blog.Post`
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.author}: {self.content[:100]}"
