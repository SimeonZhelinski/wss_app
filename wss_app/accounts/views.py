from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views, login, logout
from django.views import generic as views
from django.contrib.auth import forms as auth_forms

from wss_app.accounts.models import WssUser, Profile
from wss_app.projects.models import BuildingWithoutExistingInfrastructure, InfrastructureProject, \
    BuildingWithExistingInfrastructure


class OwnerRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class WssUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = WssUser
        fields = ('email',)


class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/log-in-page.html'
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = 'accounts/sign-up-page.html'
    form_class = WssUserCreationForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def sign_out_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/profile-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        residential_projects_count = BuildingWithoutExistingInfrastructure.objects.filter(
            project_creator=user).count() + BuildingWithExistingInfrastructure.objects.filter(
            project_creator=user).count()
        infrastructure_projects_count = InfrastructureProject.objects.filter(project_creator=user).count()
        total_projects_count = residential_projects_count + infrastructure_projects_count
        context['residential_projects_count'] = residential_projects_count
        context['infrastructure_projects_count'] = infrastructure_projects_count
        context['total_projects_count'] = total_projects_count
        return context


class ProfileUpdateView(views.UpdateView):
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
        else:
            profile.save()
        return super().form_valid(form)


class UserDeleteView(views.DeleteView):
    model = WssUser
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            return redirect('index')

        return super().delete(request, *args, **kwargs)
