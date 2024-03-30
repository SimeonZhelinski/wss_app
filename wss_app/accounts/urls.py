from django.urls import path, include
from wss_app.accounts.views import LogInUserView, SignUpUserView, sign_out_user, ProfileDetailsView, ProfileUpdateView, \
    ProfileDeleteView

urlpatterns = [
    path('login/', LogInUserView.as_view(), name='login_user'),
    path('signup/', SignUpUserView.as_view(), name='signup_user'),
    path('logout/', sign_out_user, name='logout_user'),

    path('profile/<int:pk>/',
         include([
             path("", ProfileDetailsView.as_view(), name="profile_details"),
             path("edit/", ProfileUpdateView.as_view(), name="profile_edit"),
             path("delete/", ProfileDeleteView.as_view(), name="profile_delete"),
         ]),
         )
]
