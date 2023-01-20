from django.shortcuts import render, get_object_or_404
from .models import Account


def index(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/index.html', {'accounts': accounts})


def view_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'accounts/view.html', {'account': account})
