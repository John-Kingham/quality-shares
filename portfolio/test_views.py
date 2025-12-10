from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from .models import Portfolio


class TestPortfolioView(TestCase):

    def setUp(self):
        self.title = "Test Portfolio Title"
        self.caption = "Test image caption"
        self.content = "Test portfolio content."
        self.portfolio = Portfolio(
            title=self.title,
            image_caption=self.caption,
            content=self.content,
        )
        self.portfolio.save()
        self.response = self.client.get(reverse("portfolio"))

    def tearDown(self):
        self.portfolio = None
        self.response = None

    def test_portfolio_page(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertContains(self.response, self.title)
        self.assertContains(self.response, self.caption)
        self.assertContains(self.response, self.content)
