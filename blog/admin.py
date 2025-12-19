from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Comment, Post


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = ("description",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "approved", "summary", "post", "created")
    list_filter = ("approved", "author")
    ordering = ["-created"]

    def summary(self, comment):
        """Returns summarised content that fits on the admin screen."""
        return comment.content[:50]


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "published", "created")
    search_fields = ["title", "content"]
    list_filter = ("published", "created", "category")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
