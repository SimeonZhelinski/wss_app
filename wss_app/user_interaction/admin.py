from wss_app.user_interaction.models import Review, ContactMessage

from django.contrib import admin


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'message', 'created_at']
    list_filter = ['user', 'created_at']
    list_per_page = 50
    search_fields = ['user', 'subject', 'created_at']
    search_help_text = 'Search by User, Name, Rating'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'comment', 'date_created']
    list_filter = ['user', 'date_created', 'rating']
    list_per_page = 50
    search_fields = ['user', 'date_created']
    search_help_text = 'Search by User and Date Created'
