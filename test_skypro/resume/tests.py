import unittest

from django.contrib.auth.models import User
from rest_framework.test import APIClient


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_resume(self):
        response = self.client.get('/resume/')

        self.assertEqual(response.status_code, 200)

    def test_get_one_resume(self):
        response = self.client.get('/resume/1/')

        self.assertEqual(response.status_code, 200)

    def test_patch_resume(self):
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)

        response = self.client.get('/resume/2/')

        self.assertEqual(response.status_code, 200)

        old_value = response.data['salary']

        response = self.client.patch('/resume/2/', {'salary': old_value + 1})

        self.assertNotEqual(response.data['salary'], old_value)

    def test_not_patch_resume(self):
        user = User.objects.get(username='test')

        self.client.force_authenticate(user=user)

        response = self.client.get('/resume/1/')

        self.assertEqual(response.status_code, 200)

        old_value = response.data['salary']

        response = self.client.patch('/resume/1/', {'salary': old_value + 1})

        self.assertEqual(response.status_code, 403)
