from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from .models import About


class TestAboutView(TestCase):

    def setUp(self):
        self.title = "Test About Title"
        self.image_caption = "Test image caption"
        self.content = "Test About content."
        self.about = About(
            title=self.title,
            image_caption=self.image_caption,
            content=self.content,
        )
        self.about.save()
        self.response = self.client.get(reverse("about"))

    def test_about_page(self):
        """Test that the About page contains the correct information."""
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertContains(self.response, self.title)
        self.assertContains(self.response, self.image_caption)
        self.assertContains(self.response, self.content)
