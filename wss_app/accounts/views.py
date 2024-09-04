from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views, login, logout
from django.views import generic as views


from wss_app.accounts.forms import WssUserCreationForm
from wss_app.accounts.models import WssUser, Profile
from wss_app.projects.models import BuildingWithoutExistingInfrastructure, InfrastructureProject, \
    BuildingWithExistingInfrastructure


class OwnerRequiredMixin(AccessMixin):

    def _handle_no_permission(self):
        object = super().get_object()

        if not self.request.user.is_authenticated or object.user != self.request.user:
            return self.handle_no_permission()

    def get(self, *args, **kwargs):
        return self._handle_no_permission() or \
            super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self._handle_no_permission() or \
            super().post(*args, **kwargs)


class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/log-in-page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class SignUpUserView(views.CreateView):
    template_name = 'accounts/sign-up-page.html'
    form_class = WssUserCreationForm
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def sign_out_user(request):
    logout(request)
    return redirect('index')


class ProfileMixin:
    def get_projects_count(self):
        user = self.get_object()
        residential_projects_count = (
                BuildingWithoutExistingInfrastructure.objects.filter(project_creator=user).count() +
                BuildingWithExistingInfrastructure.objects.filter(project_creator=user).count()
        )
        infrastructure_projects_count = InfrastructureProject.objects.filter(project_creator=user).count()
        total_projects_count = residential_projects_count + infrastructure_projects_count
        return residential_projects_count, infrastructure_projects_count, total_projects_count


class ProfileDetailsView(LoginRequiredMixin, views.DetailView, ProfileMixin):
    model = Profile
    template_name = "accounts/profile-details.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        residential_projects_count, infrastructure_projects_count, total_projects_count = self.get_projects_count()
        context['residential_projects_count'] = residential_projects_count
        context['infrastructure_projects_count'] = infrastructure_projects_count
        context['total_projects_count'] = total_projects_count
        return context


class ProfileUpdateView(LoginRequiredMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile-edit.html"
    fields = ("first_name", "last_name", "profile_picture")

    def get_success_url(self):
        return reverse("profile_details", kwargs={"pk": self.object.pk, })

    def form_valid(self, form):
        profile = form.save(commit=False)
        if 'profile_picture' in self.request.FILES:
            profile.profile_pic = self.request.FILES['profile_picture']
        profile.save()
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, views.DeleteView, ProfileMixin):
    model = WssUser
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        residential_projects_count, infrastructure_projects_count, total_projects_count = self.get_projects_count()
        context['residential_projects_count'] = residential_projects_count
        context['infrastructure_projects_count'] = infrastructure_projects_count
        context['total_projects_count'] = total_projects_count
        return context

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            return redirect('index')

        return super().delete(request, *args, **kwargs)
