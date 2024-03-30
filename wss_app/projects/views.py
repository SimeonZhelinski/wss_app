from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import DetailView

from wss_app.common.profile_helper import get_profile
from wss_app.projects.models import BuildingWithoutExistingInfrastructure, BuildingWithExistingInfrastructure, \
    InfrastructureProject


def create_project_index(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='projects/create-project.html', context=context)


class NewResidentialBuildingNoInfrastructureView(views.CreateView):
    queryset = BuildingWithoutExistingInfrastructure.objects.all()
    fields = ['name', 'bathroom_sink', 'kitchen_sink', 'toilet_seat', 'washing_machine', 'dishwasher', 'shower',
              'bathtub', 'building_residence', 'floor_siphon', 'project_creator']
    template_name = 'projects/create-project-no-ifr.html'
    success_url = reverse_lazy('my_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class NewResidentialBuildingWithInfrastructureView(views.CreateView):
    queryset = BuildingWithExistingInfrastructure.objects.all()
    fields = ['name', 'bathroom_sink', 'kitchen_sink', 'toilet_seat', 'washing_machine', 'dishwasher', 'shower',
              'bathtub', 'building_residence', 'floor_siphon', 'project_creator', 'building_area', 'property_area',
              'green_area', 'underground_parking_spots', 'floors']
    template_name = 'projects/create-project-with-ifr.html'
    success_url = reverse_lazy('my_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


class NewInfrastructureProjectView(views.CreateView):
    queryset = InfrastructureProject.objects.all()
    fields = ['name', 'existing_plumbing_depth', 'new_plumbing_length', 'new_plumbing_diameter', 'existing_sewer_depth',
              'new_sewer_length', 'new_sewer_diameter', 'existing_pavement']
    template_name = 'projects/create-project-infrastructure.html'
    success_url = reverse_lazy('my_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context


def my_projects(request):
    infrastructure_projects = InfrastructureProject.objects.all()
    projects_with_existing_infrastructure = BuildingWithExistingInfrastructure.objects.all()
    projects_without_existing_infrastructure = BuildingWithoutExistingInfrastructure.objects.all()

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

    profile = get_profile()
    context = {'projects': all_projects, 'profile': profile}

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
