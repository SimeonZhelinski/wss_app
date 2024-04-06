from django.urls import path

from wss_app.user_interaction.views import ContactUs, contact_success, ReviewCreateView, ReviewUpdateView, \
    ReviewDeleteView, MyReviewsView, top_reviews

urlpatterns = [
    path('contact_us/', ContactUs.as_view(), name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
    path('review/my_reviews/', MyReviewsView.as_view(), name='my_reviews'),
    path('review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('review/top_reviews/', top_reviews, name='top_reviews')
]
