from http import HTTPMethod
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic import ListView
from .forms import CommentForm
from .models import Category, Comment, Post


class CategoryListView(ListView):
    """
    Render the category list page.

    Models:
        Category
        Post

    Template:
        blog/category_list.html

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
        Return the template's context.

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
    Render the post list page.

    Models:
        Post

    Template:
        blog/post_list.html

    Context:
        "posts" (QuerySet): All published posts.
    """

    model = Post
    queryset = Post.objects.filter(published=True)
    context_object_name = "posts"


def post_detail(request, slug):
    """
    Return the post details page for a post and save any new comments.

    If the request method is POST then the user has submitted a new comment.
    Save the comment before returning the post details page.

    Args:
        request (HttpRequest):
            A GET or POST request. If it's a POST request, it contains data
            for a new comment.
        slug (str): The blog post slug.

    Models:
        Post
        Comment

    Template:
        blog/post_detail.html

    Context:
        post (Post): The blog post.
        comments (Comment): The blog post's comments.
        comment_form (CommentForm): A form for the Comment model.

    Returns:
        HttpResponse: Contains the blog details page.
    """
    published_posts = Post.objects.filter(published=True)
    post = get_object_or_404(published_posts, slug=slug)
    if request.method == HTTPMethod.POST:
        _save_comment(request, post)
    comment_form = CommentForm()
    context = {
        "post": post,
        "comments": post.comments.all().order_by("-created"),
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context)


def _save_comment(request, post):
    """
    Save a new comment.

    Args:
        request (HttpRequest):
            A POST request that contains CommentForm data for the new comment.
        post (Post): The new comment's related blog post.

    Models:
        Comment
        Post

    Messages:
        SUCCESS: If the new comment is saved.
        ERROR: If there is an error and the comment isn't saved.
    """
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        message = "Your comment is awaiting approval."
        messages.add_message(request, messages.SUCCESS, message)
    else:
        message = "Error: Your comment has not been saved."
        messages.add_message(request, messages.ERROR, message)


def edit_comment_view(request, slug, comment_id):
    """
    Save an edited comment.

    Args:
        request (HttpRequest):
            A POST request that contains CommentForm data for the comment.
        slug (str): The related post's slug.
        comment_id (int): The comment's ID.

    Models:
        Comment

    Messages:
        SUCCESS: If the updated comment is saved.
        ERROR: If there is an error and the comment isn't saved.
    """
    if request.method == HTTPMethod.POST:
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and request.user == comment.author:
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            message = "Your edited comment is awaiting approval."
            messages.add_message(request, messages.SUCCESS, message)
        else:
            message = "Error: Your comment has not been updated."
            messages.add_message(request, messages.ERROR, message)
    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def delete_comment_view(request, slug, comment_id):
    """
    Delete a comment and reload the post details page.

    Only delete the comment ff the request's user is the comment's author.

    Args:
        request (HTTPRequest): A request where the user is the comment author.
        slug (str): The slug for the comment's post.
        comment_id (int): The comment's ID.

    Models:
        Comment

    Template:
        blog/post_details.html

    Messages:
        SUCCESS: If the comment is deleted from the database.
        ERROR: If the request's user isn't the comment's author.

    Returns:
        HttpResponseRedirect:
            Redirect back to the post detail page for the comment's post.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        comment.delete()
        message = "Your comment has been deleted."
        messages.add_message(request, messages.SUCCESS, message)
    else:
        message = "You cannot delete someone else's comment."
        messages.add_message(request, messages.ERROR, message)
    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
