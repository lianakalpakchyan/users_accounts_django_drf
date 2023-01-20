from django.urls import resolve
from django.test import SimpleTestCase

from accounts.api_views import AccountViewset


class APIUrlsTest(SimpleTestCase):
    def test_accounts(self):
        path = resolve('/api/accounts/')
        self.assertEquals(path.func.cls, AccountViewset)
