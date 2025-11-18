from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class RedactorListViewTest(TestCase):

    def setUp(self):
        # Create users (including one for login)
        self.user = get_user_model().objects.create_user(
            username="admin_user",
            password="adminpass123",
            year_of_experience=10,
        )
        self.client.login(username="admin_user", password="adminpass123")

        self.red1 = get_user_model().objects.create_user(
            username="vasyl",
            password="pass1234",
            year_of_experience=3
        )
        self.red2 = get_user_model().objects.create_user(
            username="andrii",
            password="pass1234",
            year_of_experience=2
        )

    def test_page_loads_successfully(self):
        url = reverse("main:redactor-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "vasyl")
        self.assertContains(response, "andrii")

    def test_search_filters_correctly(self):
        url = reverse("main:redactor-list")
        response = self.client.get(url, {"username": "vas"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "vasyl")
        self.assertNotContains(response, "andrii")

    def test_search_is_case_insensitive(self):
        url = reverse("main:redactor-list")
        response = self.client.get(url, {"username": "VASY"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "vasyl")

    def test_search_form_in_context(self):
        url = reverse("main:redactor-list")
        response = self.client.get(url)

        self.assertIn("search_form", response.context)
