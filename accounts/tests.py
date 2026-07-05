from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class CustomUserModelTests(TestCase):
    def test_custom_user_is_active_auth_model(self):
        self.assertEqual(get_user_model(), CustomUser)


class CustomUserAdminTests(TestCase):
    def test_custom_user_registered_in_admin(self):
        self.assertIn(CustomUser, admin.site._registry)


class CustomUserViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="existing",
            email="existing@example.com",
            **{"password": "StrongPass123"},
        )

    def test_list_view(self):
        response = self.client.get(reverse("accounts:user-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "existing")

    def test_detail_view(self):
        response = self.client.get(reverse("accounts:user-detail", args=[self.user.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "existing@example.com")

    def test_create_view(self):
        response = self.client.post(
            reverse("accounts:user-create"),
            {
                "username": "new-user",
                "email": "new-user@example.com",
                "password1": "StrongPass123",
                "password2": "StrongPass123",
            },
        )

        self.assertRedirects(response, reverse("accounts:user-list"))
        self.assertTrue(CustomUser.objects.filter(username="new-user").exists())

    def test_update_view(self):
        response = self.client.post(
            reverse("accounts:user-update", args=[self.user.pk]),
            {
                "username": "existing",
                "email": "updated@example.com",
                "is_active": "on",
                "is_staff": "",
            },
        )

        self.assertRedirects(response, reverse("accounts:user-list"))
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "updated@example.com")
