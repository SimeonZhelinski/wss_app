from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('', include('wss_app.common.urls')),
                  path('accounts/', include('wss_app.accounts.urls')),
                  path('projects/', include('wss_app.projects.urls')),
                  path('user_interaction/', include('wss_app.user_interaction.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
