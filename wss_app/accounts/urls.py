from django.urls import path

from wss_app.accounts import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='signin')
]