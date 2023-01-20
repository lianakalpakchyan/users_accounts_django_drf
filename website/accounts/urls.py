from django.urls import path
from .views import index, view_account

urlpatterns = [
    path('', index, name='account_list'),
    path('<int:pk>', view_account, name='account_view'),
]
