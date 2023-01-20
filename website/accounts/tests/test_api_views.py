from django.contrib.auth import get_user_model
from django.core.cache import cache

from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import Account


class AccountViewsetTest(APITestCase):
    def setUp(self) -> None:
        cache.clear()

        self.user = get_user_model().objects.create_user(
            username="test-username",
            password="test-pass-1234",
        )
        self.account = Account.objects.create(name="test-name", owner=self.user)
        self.GET_PATH = '/api/accounts/'
        self.TOKEN = '/api-auth/token/'

    def test_get_with_and_without_authentication(self):
        path = self.GET_PATH
        response = self.client.get(path)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        token_path = self.TOKEN
        response = self.client.post(
            path=token_path,
            data={"username": "test-username", "password": "test-pass-1234"},
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['access']}"
        )

        response = self.client.get(path)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'][0]['id'], 1)
        self.assertEquals(response.data['results'][0]['url'], 'http://testserver/api/accounts/1/')
