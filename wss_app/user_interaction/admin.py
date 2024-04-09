from django.contrib import admin

from wss_app.user_interaction.models import ContactMessage, Review


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'message', 'created_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass




