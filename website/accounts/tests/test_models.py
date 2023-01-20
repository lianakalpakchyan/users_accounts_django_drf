from django.contrib.auth import get_user_model
from django.test import TestCase
from accounts.models import Account


class AccountTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test-username",
            password="test-pass-1234",
        )
        self.account = Account.objects.create(name="test-name", owner=self.user)

    def test_str_method(self):
        self.assertEquals(str(self.account), self.account.name)

    def test_fields_account_model(self):
        self.assertEquals(self.account.owner, self.user)
