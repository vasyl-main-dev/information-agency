from django.test import TestCase
from django.urls import reverse
from main.models import Redactor, Newspaper, Topic


class NewspaperCreateViewTest(TestCase):

    def setUp(self):
        # Створення користувача
        self.user = Redactor.objects.create_user(
            username="testuser", password="password123", year_of_experience=5
        )

        # Створення теми
        self.topic = Topic.objects.create(name="Politics")

        # Логін
        self.client.login(username="testuser", password="password123")

    def test_newspaper_create(self):
        url = reverse("main:newspaper-create")

        data = {
            "title": "Breaking News",
            "content": "Something very important happened.",
            "topics": [self.topic.id],
            "publishers": [self.user.id],
        }

        response = self.client.post(url, data)

        # Перевіряємо redirect після створення
        self.assertEqual(response.status_code, 302)

        # Перевіряємо що запис створився
        newspaper = Newspaper.objects.first()
        self.assertIsNotNone(newspaper)

        # Перевіряємо поля
        self.assertEqual(newspaper.title, "Breaking News")
        self.assertEqual(newspaper.content, "Something very important happened.")

        # Багато-до-багатьох
        self.assertIn(self.topic, newspaper.topics.all())
        self.assertIn(self.user, newspaper.publishers.all())
