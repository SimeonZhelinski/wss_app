from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views, View

from wss_app.accounts.views import OwnerRequiredMixin
from wss_app.common.profile_helper import get_profile
from wss_app.projects.models import InfrastructureProject, BuildingWithoutExistingInfrastructure, \
    BuildingWithExistingInfrastructure
from wss_app.user_interaction.forms import ContactMessageForm, ReviewForm
from wss_app.user_interaction.models import ContactMessage, Review


class ContactUs(LoginRequiredMixin, views.CreateView):
    model = ContactMessage
    form_class = ContactMessageForm
    template_name = 'user_interaction/contact-us.html'
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


def contact_success(request):
    return render(request, 'user_interaction/contact-success.html')


class ReviewCreateView(LoginRequiredMixin, views.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'user_interaction/review-create.html'
    success_url = reverse_lazy('my_reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_projects'] = self.has_projects(self.request.user)
        return context

    def has_projects(self, user):
        return any([
            InfrastructureProject.objects.filter(project_creator=user).exists(),
            BuildingWithExistingInfrastructure.objects.filter(project_creator=user).exists(),
            BuildingWithoutExistingInfrastructure.objects.filter(project_creator=user).exists()
        ])


class ReviewUpdateView(LoginRequiredMixin, OwnerRequiredMixin, views.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'user_interaction/review-edit.html'
    success_url = reverse_lazy('my_reviews')

    def get_object(self, queryset=None):
        return get_object_or_404(Review, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDeleteView(LoginRequiredMixin, OwnerRequiredMixin, views.DeleteView):
    model = Review
    success_url = reverse_lazy('my_reviews')


class MyReviewsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_reviews = Review.objects.filter(user=request.user)
        return render(request, 'user_interaction/profile-reviews.html', {'user_reviews': user_reviews})


def top_reviews(request):
    top_reviews = Review.objects.order_by('-rating')[:5]
    return render(request, 'user_interaction/top-reviews.html', {'top_reviews': top_reviews})
