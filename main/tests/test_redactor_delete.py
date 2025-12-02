from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class RedactorDeleteViewTest(TestCase):

    def setUp(self):
        self.User = get_user_model()

        self.user = self.User.objects.create_user(
            username="user1", password="password123", year_of_experience=3
        )

        self.other_user = self.User.objects.create_user(
            username="user2", password="password123", year_of_experience=7
        )

        self.client.login(username="user1", password="password123")

    def test_user_can_delete_self(self):
        """User should be able to delete their own account"""
        url = reverse("main:redactor-delete", args=[self.user.id])

        response = self.client.post(url, follow=True)

        # Статус ОК після redirect (бо follow=True)
        self.assertEqual(response.status_code, 200)

        # Юзера більше немає
        self.assertFalse(self.User.objects.filter(id=self.user.id).exists())

        # Юзер вилогінений
        self.assertNotIn("_auth_user_id", self.client.session)

        # Messages
        messages = list(response.context["messages"])
        self.assertGreater(len(messages), 0)
        self.assertIn("account", messages[0].message.lower())

    def test_user_cannot_delete_another_user(self):
        url = reverse("main:redactor-delete", args=[self.other_user.id])

        response = self.client.post(url, follow=True)

        # Після redirect сторінка 200
        self.assertEqual(response.status_code, 200)

        # Інший юзер НЕ видалений
        self.assertTrue(self.User.objects.filter(id=self.other_user.id).exists())

        # Перевіряємо messages.error
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertIn("delete your own account", messages[0].message.lower())
