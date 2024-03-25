from django.shortcuts import render
from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from wss_app.accounts.models import Profile
from wss_app.common.models import ContactMessage
from wss_app.common.profile_helper import get_profile


def index(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='common/index.html', context=context)


def objective_page(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='common/objective.html', context=context)


class ContactUs(views.CreateView):
    queryset = ContactMessage.objects.all()
    fields = ['name', 'email', 'message']
    template_name = 'common/contact-us.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context
