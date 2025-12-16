from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Post


class TestPostViews(TestCase):

    def setUp(self):
        # create two posts, one published, one draft.
        self.user = User.objects.create_superuser(
            username="test-username",
            password="test-password",
            email="text@example.com",
        )
        self.published_title = "Published Post Title"
        self.published_description = "Published Post Description"
        self.published_content = "Published Post Content"
        self.published_slug = "published-post-slug"
        self.published_post = Post(
            author=self.user,
            published=True,
            title=self.published_title,
            description=self.published_description,
            content=self.published_content,
            slug=self.published_slug,
        )
        self.published_post.save()
        self.draft_title = "Draft Post Title"
        self.draft_post = Post(
            author=self.user,
            title=self.draft_title,
        )
        self.draft_post.save()

    def tearDown(self):
        self.user = None
        self.published_post = None
        self.draft_post = None

    def test_post_list_view(self):
        """Test that the post list page contains the correct information"""
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_title)
        self.assertContains(response, self.published_description)
        self.assertContains(response, self.published_slug)
        self.assertNotContains(response, self.draft_title)

    def test_post_detail_view(self):
        """Test that the post detail page contains the correct information"""
        post_detail_url = reverse("post_detail", args=[self.published_slug])
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, self.published_title)
        self.assertContains(response, self.published_content)
