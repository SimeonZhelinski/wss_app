from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views, View
from django.views.generic import DetailView

from wss_app.accounts.models import Profile
from wss_app.common.profile_helper import get_profile
from wss_app.projects.forms import BuildingWithoutExistingInfrastructureCreateForm, \
    BuildingWithExistingInfrastructureCreateForm, InfrastructureProjectCreateForm
from wss_app.projects.models import BuildingWithoutExistingInfrastructure, BuildingWithExistingInfrastructure, \
    InfrastructureProject


def create_project_index(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='projects/create-project.html', context=context)


class NewResidentialBuildingNoInfrastructureView(views.CreateView):
    model = BuildingWithoutExistingInfrastructure
    form_class = BuildingWithoutExistingInfrastructureCreateForm
    template_name = 'projects/create-project-no-ifr.html'
    success_url = reverse_lazy('my_projects')

    def form_valid(self, form):
        form.instance.project_creator = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class NewResidentialBuildingWithInfrastructureView(views.CreateView):
    model = BuildingWithExistingInfrastructure
    form_class = BuildingWithExistingInfrastructureCreateForm
    template_name = 'projects/create-project-with-ifr.html'
    success_url = reverse_lazy('my_projects')

    def form_valid(self, form):
        form.instance.project_creator = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class NewInfrastructureProjectView(views.CreateView):
    model = InfrastructureProject
    form_class = InfrastructureProjectCreateForm
    template_name = 'projects/create-project-infrastructure.html'
    success_url = reverse_lazy('my_projects')

    def form_valid(self, form):
        form.instance.project_creator = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class MyProjectsView(LoginRequiredMixin, View):
    def get(self, request):
        wss_user = request.user

        infrastructure_projects = InfrastructureProject.objects.filter(project_creator=wss_user)
        projects_with_existing_infrastructure = BuildingWithExistingInfrastructure.objects.filter(
            project_creator=wss_user)
        projects_without_existing_infrastructure = BuildingWithoutExistingInfrastructure.objects.filter(
            project_creator=wss_user)

        all_projects = list(infrastructure_projects) + \
                       list(projects_with_existing_infrastructure) + \
                       list(projects_without_existing_infrastructure)

        for project in all_projects:
            if isinstance(project, InfrastructureProject):
                project.project_type = "InfrastructureProject"
            elif isinstance(project, BuildingWithExistingInfrastructure):
                project.project_type = "BuildingWithExistingInfrastructure"
            elif isinstance(project, BuildingWithoutExistingInfrastructure):
                project.project_type = "BuildingWithoutExistingInfrastructure"

        context = {'projects': all_projects, 'user': wss_user}
        return render(request, 'projects/profile-projects.html', context)


class ResidentialBuildingNoInfrastructureDetailView(views.DetailView):
    model = BuildingWithoutExistingInfrastructure
    template_name = 'projects/project-details-no-ifr.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['slug'] = self.kwargs.get(self.slug_url_kwarg)
        context['project_name'] = self.object.name if self.object else None
        return context


class ResidentialBuildingWithInfrastructureDetailView(views.DetailView):
    model = BuildingWithExistingInfrastructure
    template_name = 'projects/project-details-with-ifr.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['slug'] = self.kwargs.get(self.slug_url_kwarg)
        context['project_name'] = self.object.name if self.object else None
        return context


class InfrastructureProjectDetailView(views.DetailView):
    model = InfrastructureProject
    template_name = 'projects/project-details-infrastructure.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['slug'] = self.kwargs.get(self.slug_url_kwarg)
        context['project_name'] = self.object.name if self.object else None
        return context


class ResidentialBuildingNoInfrastructureEditView(views.UpdateView):
    queryset = BuildingWithoutExistingInfrastructure.objects.all()
    template_name = 'projects/edit-project-no-ifr.html'
    fields = '__all__'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context


class ResidentialBuildingWithInfrastructureEditView(views.UpdateView):
    queryset = BuildingWithExistingInfrastructure.objects.all()
    template_name = 'projects/edit-project-with-ifr.html'
    fields = '__all__'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context


class InfrastructureProjectEditView(views.UpdateView):
    queryset = InfrastructureProject.objects.all()
    template_name = 'projects/edit-project-infrastructure.html'
    fields = '__all__'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context


class ResidentialBuildingNoInfrastructureDeleteView(views.DeleteView):
    queryset = BuildingWithoutExistingInfrastructure.objects.all()
    template_name = 'projects/delete-project-no-ifr.html'
    success_url = 'projects/profile-projects.html'
    form_class = modelform_factory(
        BuildingWithoutExistingInfrastructure,
        fields='__all__',
    )
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class ResidentialBuildingWithInfrastructureDeleteView(views.DeleteView):
    queryset = BuildingWithExistingInfrastructure.objects.all()
    template_name = 'projects/delete-project-with-ifr.html'
    success_url = 'projects/profile-projects.html'
    form_class = modelform_factory(
        BuildingWithExistingInfrastructure,
        fields='__all__',
    )
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class InfrastructureProjectDeleteView(views.DeleteView):
    queryset = InfrastructureProject.objects.all()
    template_name = 'projects/delete-project-infrastructure.html'
    success_url = 'projects/profile-projects.html'
    form_class = modelform_factory(
        InfrastructureProject,
        fields='__all__',
    )
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context
