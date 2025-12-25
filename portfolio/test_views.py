from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from .models import Portfolio


class TestPortfolioView(TestCase):

    def setUp(self):
        self.title = "Test Portfolio Title"
        self.image_caption = "Test image caption"
        self.content = "Test portfolio content."
        self.portfolio = Portfolio(
            title=self.title,
            image_caption=self.image_caption,
            content=self.content,
        )
        self.portfolio.save()
        self.response = self.client.get(reverse("portfolio"))

    def test_portfolio_page(self):
        """Test that the Portfolio page contains the correct information."""
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertContains(self.response, self.title)
        self.assertContains(self.response, self.image_caption)
        self.assertContains(self.response, self.content)
