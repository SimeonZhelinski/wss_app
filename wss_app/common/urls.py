from django.urls import path

from wss_app.common.views import index, objective_page

urlpatterns = [
    path("", index, name="index"),
    path("common/", objective_page, name="objective"),

]
