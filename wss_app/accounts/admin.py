from django.contrib import admin

from wss_app.accounts.models import WssUser, Profile


@admin.register(WssUser)
class WssUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'date_joined']
    list_display_links = ['id', 'email', 'date_joined']
    list_filter = ['date_joined']
    list_per_page = 50
    search_fields = ['email']
    search_help_text = 'Search by Email'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    list_display_links = ['user', 'first_name', 'last_name']
    list_per_page = 50
    search_fields = ['user', 'first_name', 'last_name']
    search_help_text = 'Search by User, First Name or Last Name'
