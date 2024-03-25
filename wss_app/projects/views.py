from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
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
