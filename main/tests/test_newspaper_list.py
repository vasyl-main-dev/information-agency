from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from main.models import Newspaper, Topic


class NewspaperListViewTest(TestCase):
    def setUp(self):
        # Create user to satisfy LoginRequired (якщо потрібно)
        self.user = get_user_model().objects.create_user(
            username="tester",
            password="password123",
            year_of_experience=5,
        )
        self.client.login(username="tester", password="password123")

        # Створюємо теми
        self.topic = Topic.objects.create(name="Politics")

        # Створюємо газети
        self.news1 = Newspaper.objects.create(
            title="Government reforms",
            content="Some long text..."
        )
        self.news1.topics.add(self.topic)

        self.news2 = Newspaper.objects.create(
            title="Sports Weekly",
            content="Sport content..."
        )
        self.news2.topics.add(self.topic)

    def test_page_loads_successfully(self):
        url = reverse("main:newspaper-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Government reforms")
        self.assertContains(response, "Sports Weekly")

    def test_search_filters_correctly(self):
        url = reverse("main:newspaper-list")
        response = self.client.get(url, {"title": "government"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Government reforms")
        self.assertNotContains(response, "Sports Weekly")

    def test_search_is_case_insensitive(self):
        url = reverse("main:newspaper-list")
        response = self.client.get(url, {"title": "SPORTS"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sports Weekly")

    def test_search_form_in_context(self):
        url = reverse("main:newspaper-list")
        response = self.client.get(url)

        self.assertIn("search_form", response.context)
