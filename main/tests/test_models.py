from django.contrib.auth import get_user_model
from django.test import TestCase

from main.models import Topic, Newspaper


class TopicModelTest(TestCase):
    def test_str_topic(self):
        topic = Topic.objects.create(name="Politic")
        self.assertEqual(str(topic), topic.name)


class RedactorModelTest(TestCase):
    def test_str_redactor(self):
        redactor = get_user_model().objects.create_user(
            username="redactor",
            first_name="John",
            last_name="Doe",
            year_of_experience=10,
            password="testpassword123",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username}: {redactor.first_name} {redactor.last_name}",
        )


class NewspaperModelTest(TestCase):
    def setUp(self):
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            first_name="Max",
            last_name="Mad",
            year_of_experience=7,
            password="superpassword123",
        )
        self.topic = Topic.objects.create(name="Tech")

    def test_str_newspaper(self):
        newspaper = Newspaper.objects.create(
            title="The new time",
            content="Today is perfect time for something new",
        )
        self.assertEqual(
            str(newspaper), f"{newspaper.title} ({newspaper.published_date:%Y-%m-%d})"
        )

    def test_published_date_auto_set(self):
        newspaper = Newspaper.objects.create(
            title="The date test",
            content="Test content",
        )
        self.assertIsNotNone(newspaper.published_date)

    def test_topics_and_publishers_many_to_many(self):
        newspaper = Newspaper.objects.create(
            title="Relation test",
            content="Testing m2m",
        )
        newspaper.topics.add(self.topic)
        newspaper.publishers.add(self.redactor)

        self.assertIn(self.topic, newspaper.topics.all())
        self.assertIn(self.redactor, newspaper.publishers.all())
