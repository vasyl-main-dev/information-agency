from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from main.models import Newspaper, Topic


class NewspaperDeleteViewTest(TestCase):

    def setUp(self):
        self.User = get_user_model()

        # author
        self.author = self.User.objects.create_user(
            username="author",
            password="pass123",
            year_of_experience=5
        )

        # another user
        self.other_user = self.User.objects.create_user(
            username="intruder",
            password="pass123",
            year_of_experience=3
        )

        # Topic
        self.topic = Topic.objects.create(name="Tech")

        # Newspaper
        self.newspaper = Newspaper.objects.create(
            title="Test News",
            content="Some content..."
        )
        self.newspaper.topics.add(self.topic)
        self.newspaper.publishers.add(self.author)

    def test_author_can_delete_newspaper(self):
        self.client.login(username="author", password="pass123")

        url = reverse("main:newspaper-delete", args=[self.newspaper.id])

        response = self.client.post(url, follow=True)

        # Newspaper deleted
        self.assertFalse(Newspaper.objects.filter(id=self.newspaper.id).exists())

    def test_other_user_cannot_delete_newspaper(self):
        """Non-author must NOT be able to delete the newspaper"""

        self.client.login(username="intruder", password="pass123")

        url = reverse("main:newspaper-delete", args=[self.newspaper.id])
        response = self.client.post(url, follow=True)

        # Redirect expected
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/")

        # Newspaper must still exist
        self.assertTrue(Newspaper.objects.filter(id=self.newspaper.id).exists())

        # Error message must be shown
        messages = list(response.context["messages"])
        self.assertGreater(len(messages), 0)
        # self.assertIn("not allowed", messages[0].message.lower())
