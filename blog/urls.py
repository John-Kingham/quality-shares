from django.urls import path
from . import views

urlpatterns = [
    path("archive/", views.PostListView.as_view(), name="post-list"),
    path("<slug:slug>/", views.post_detail, name="post-detail"),
]
