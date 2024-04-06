from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from wss_app.common.profile_helper import get_profile
from wss_app.user_interaction.forms import ContactMessageForm
from wss_app.user_interaction.models import ContactMessage


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
    return render(request, 'user_interaction/contact_success.html')
