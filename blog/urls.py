from django.urls import path
from . import views

urlpatterns = [
    path("archive/", views.PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.edit_comment_view,
        name="edit_comment",
    ),
    path("", views.CategoryListView.as_view(), name="category_list"),
]
