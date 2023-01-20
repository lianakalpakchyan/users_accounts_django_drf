from django.urls import path, include
from .api_views import AccountViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('accounts', AccountViewset)

urlpatterns = [
    path('', include(router.urls)),
]
