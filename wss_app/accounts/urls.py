from django.urls import path, include
from wss_app.accounts.views import LogInUserView, SignUpUserView, sign_out_user, ProfileDetailsView, ProfileUpdateView, \
    UserDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LogInUserView.as_view(), name='login_user'),
    path('signup/', SignUpUserView.as_view(), name='signup_user'),
    path('logout/', sign_out_user, name='logout_user'),

    path('profile/<int:pk>/',
         include([
             path("", ProfileDetailsView.as_view(), name="profile_details"),
             path("edit/", ProfileUpdateView.as_view(), name="profile_edit"),
             path("delete/", UserDeleteView.as_view(), name="profile_delete"),
         ]),
         ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
