from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Category, Post


class CategoryListView(ListView):
    """
    Renders the category list page.

    Models:
        :model:`blog.Category`
        :model:`blog.Post`

    Template:
        :template:`blog/category_list.html`

    Context:
        "categories" (QuerySet): All categories
        "category_posts" (dict): The key is a category with published posts and
         the value is the published posts.
    """

    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        """
        Returns the template's context.

        Return:
            Context:
                "categories" (QuerySet): All categories
                "category_posts" (dict): The key is a category with published
                posts and the value is the published posts.
        """

        context = super().get_context_data(**kwargs)
        category_posts = {}
        num_visible_posts = 4
        for category in context["categories"]:
            published_posts = category.blog_posts.filter(published=True)
            if published_posts:
                category_posts[category] = published_posts[:num_visible_posts]
        context["category_posts"] = category_posts
        return context


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
