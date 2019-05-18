from django.test import TestCase
from django import test
# Create your tests here.

class URLTests(test.TestCase):
    def test_homepage(self):
        response = self.client.get(path='http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        print(str(response.content))
        print('Тест пройден, главная вернула код 200')