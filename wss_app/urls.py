
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('wss_app.common.urls')),
    path('accounts/', include('wss_app.accounts.urls')),
    path('projects/', include('wss_app.projects.urls')),
]
