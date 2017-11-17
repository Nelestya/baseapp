from django.test import TestCase
from django.urls import reverse
from django.test.utils import setup_test_environment
# Create your tests here.
class BaseappIndexViewTests(TestCase):
    def test_page(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('baseapp:index'))
        self.assertEqual(response.status_code, 200)