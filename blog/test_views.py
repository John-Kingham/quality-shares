from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Category, Comment, Post


class TestBlogViews(TestCase):
    """Test view for the blog app."""

    def setUp(self):
        """
        Set up two posts, one published, one draft, each attached to a
        different category. Give the published post two comments; one approved
        and one not approved.
        """
        # Set up two categories
        self.category_with_published_post = Category(name="Category 1")
        self.category_with_published_post.save()
        self.category_no_published_post = Category(name="Category 2")
        self.category_no_published_post.save()

        # Set up a published post
        self.user_password = "test-password"
        self.user = User.objects.create_superuser(
            username="test-username",
            password=self.user_password,
            email="test@example.com",
        )
        self.published_post = Post(
            author=self.user,
            published=True,
            category=self.category_with_published_post,
            title="Published Post Title",
            description="Published post description.",
            content="Published post content.",
            slug="published-post-slug",
        )
        self.published_post.save()

        # Give the published post one approved comment, one unapproved, with
        # the unapproved comment written by a different author.
        self.approved_comment = Comment(
            post=self.published_post,
            author=self.user,
            content="Approved comment content.",
            approved=True,
        )
        self.approved_comment.save()
        self.unapproved_comment_author = User.objects.create_superuser(
            username="unapproved-comment-author",
            password="test-password",
            email="test@example.com",
        )
        self.unapproved_comment = Comment(
            post=self.published_post,
            author=self.unapproved_comment_author,
            content="Unapproved comment content.",
            approved=False,
        )
        self.unapproved_comment.save()
        self.published_post.save()

        # Set up a draft post
        self.draft_post = Post(
            author=self.user,
            title="Draft Post Title",
            category=self.category_no_published_post,
        )
        self.draft_post.save()

    def test_post_list_view(self):
        """Test that the post list page contains the correct information."""
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.description)
        self.assertContains(response, self.published_post.slug)
        self.assertContains(response, self.published_post.category.name)
        self.assertNotContains(response, self.draft_post.title)
        self.assertNotContains(response, self.draft_post.category.name)

    def test_post_detail_view(self):
        """Test that the post detail page contains the correct information."""
        post_detail_url = reverse(
            "post_detail", args=[self.published_post.slug]
        )
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.content)
        self.assertContains(response, self.published_post.category.name)
        self.assertContains(response, self.approved_comment.content)
        self.assertNotContains(response, self.unapproved_comment.content)

    def test_category_list_view(self):
        """Test that the category list (home) page is rendering correctly."""
        response = self.client.get(reverse("category_list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.category.name)
        self.assertNotContains(response, self.draft_post.title)
        self.assertNotContains(response, self.draft_post.category.name)

    def test_new_comment_submission(self):
        """Test posting of a new comment."""
        self.client.login(
            username=self.user.username, password=self.user_password
        )
        comment_form_data = {"content": "Comment body"}
        response = self.client.post(
            reverse("post_detail", args=[self.published_post.slug]),
            comment_form_data,
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Your comment is awaiting approval.")
        self.assertContains(response, comment_form_data["content"])
