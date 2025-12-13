from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Comment, Post


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "approved", "summary", "post")
    list_filter = ("author", "approved")

    def summary(self, comment):
        max_length = 50
        content_summary = comment.content[:max_length]
        suffix = "..." if len(content_summary) == max_length else ""
        return content_summary + suffix


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "published", "created")
    search_fields = ["title", "content"]
    list_filter = ("published", "created")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
