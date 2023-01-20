from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ['id', 'url', 'name', 'created_on', 'owner', 'updated_on']
