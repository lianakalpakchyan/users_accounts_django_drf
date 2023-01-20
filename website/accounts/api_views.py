from rest_framework import viewsets, permissions
from .models import Account
from .serializers import AccountSerializer


class AccountViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    http_method_names = ('get', 'retrieve',)
