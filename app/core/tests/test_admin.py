from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@admin.com',
            password = 'password 123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@test.com',
            password = 'test123',
            name = 'Test User'
        )

    def test_users_listed(self):
        path = reverse('admin:core_user_changelist')
        res = self.client.get(path)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        path = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(path)

        self.assertEqual(res.status_code, 200)