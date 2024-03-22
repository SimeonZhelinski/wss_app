from django.urls import path

from wss_app.common.views import index

urlpatterns = [
    path("", index, name="index")
]
