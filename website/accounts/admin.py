from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on', 'updated_on', 'owner')
    list_display_links = ('id', 'name')
    