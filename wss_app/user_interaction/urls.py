from django.urls import path

from wss_app.user_interaction.views import ContactUs, contact_success

urlpatterns = [
    path('contact_us/', ContactUs.as_view(), name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
]
