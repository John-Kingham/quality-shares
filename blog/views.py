from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    """
    Renders the post list page.

    Models:
        :model:`blog.Post`

    Template:
        :template:`blog/post_list.html`

    Context:
        posts (QuerySet): All published posts.
    """

    model = Post
    queryset = Post.objects.filter(published=True)
    context_object_name = "posts"


def post_detail(request, slug):
    """
    Returns the post details page for a post.

    Args:
        request (HttpRequest):
            A GET request.
        slug (str): The ID of a :model:`blog.Post`.

    Models:
        :model:`blog.Post`

    Template:
        :template:`blog/post_detail.html`

    Context:
        post (:model:`blog.Post`): The blog post.

    Returns:
        HttpResponse: Contains the blog details page.
    """
    published_posts = Post.objects.filter(published=True)
    post = get_object_or_404(published_posts, slug=slug)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)
