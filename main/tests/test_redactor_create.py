from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class RedactorCreateViewTest(TestCase):

    def setUp(self):
        # Потрібно залогінити користувача, бо CreateView доступний тільки авторизованим
        self.existing_user = get_user_model().objects.create_user(
            username="admin", password="adminpass123", year_of_experience=10
        )
        self.client.login(username="admin", password="adminpass123")

    def test_redactor_create(self):
        url = reverse("main:redactor-create")

        data = {
            "username": "new_redactor",
            "password1": "strongPass123!",
            "password2": "strongPass123!",
            "year_of_experience": 5,
            "first_name": "John",
            "last_name": "Doe",
        }

        response = self.client.post(url, data)

        # Успішний redirect після створення
        self.assertEqual(response.status_code, 302)

        # Перевіряємо чи створився обʼєкт
        new_redactor = get_user_model().objects.filter(username="new_redactor").first()
        self.assertIsNotNone(new_redactor)

        # Перевіряємо правильність даних
        self.assertEqual(new_redactor.year_of_experience, 5)
        self.assertEqual(new_redactor.first_name, "John")
        self.assertEqual(new_redactor.last_name, "Doe")

    def test_invalid_form_does_not_create_user(self):
        url = reverse("main:redactor-create")

        # password mismatch → форма має бути невалідна
        data = {
            "username": "bad_user",
            "password1": "pass123",
            "password2": "different_pass",
            "year_of_experience": 2,
        }

        response = self.client.post(url, data)

        # Форма повертає 200 зі сторінкою, а не redirect
        self.assertEqual(response.status_code, 200)

        # Перевіряємо що юзер НЕ створився
        self.assertFalse(get_user_model().objects.filter(username="bad_user").exists())
