from django.urls import path

from wss_app.common.views import index, objective_page, ContactUs

urlpatterns = [
    path("", index, name="index"),
    path("common/", objective_page, name="objective"),
    path("contact_us/", ContactUs.as_view(), name="contact_us")
]
