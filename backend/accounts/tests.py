from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class AuthAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_with_bad_password(self):
        url = reverse("api-register")
        resp = self.client.post(url, {"username": "u1", "password": "123"}, format="json")
        self.assertEqual(resp.status_code, 400)

    def test_register_and_login(self):
        reg_url = reverse("api-register")
        login_url = reverse("api-login")
        # good password (meets defaults in settings)
        resp = self.client.post(reg_url, {"username": "u2", "password": "My$ecure123"}, format="json")
        self.assertEqual(resp.status_code, 201)
        # login
        resp2 = self.client.post(login_url, {"username": "u2", "password": "My$ecure123"}, format="json")
        self.assertEqual(resp2.status_code, 200)
