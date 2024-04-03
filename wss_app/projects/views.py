from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views, View
from django.views.generic import DetailView

from wss_app.accounts.models import Profile
from wss_app.common.profile_helper import get_profile
from wss_app.projects.calculations import ResidenceBuildingWithoutInfrastructureCalculator, \
    ResidenceBuildingWithInfrastructureCalculator
from wss_app.projects.forms import BuildingWithoutExistingInfrastructureCreateForm, \
    BuildingWithExistingInfrastructureCreateForm, InfrastructureProjectCreateForm, \
    BuildingWithoutExistingInfrastructureEditForm, BuildingWithExistingInfrastructureEditForm, \
    InfrastructureProjectEditForm, InfrastructureProjectDeleteForm
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
        building = self.get_object()
        calculator = ResidenceBuildingWithoutInfrastructureCalculator(building)
        plumbing_info = calculator.calculate()
        profile = get_profile()
        context['plumbing_info'] = plumbing_info
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
        building = self.get_object()
        calculator = ResidenceBuildingWithInfrastructureCalculator(building)
        plumbing_info = calculator.calculate()
        profile = get_profile()
        context['plumbing_info'] = plumbing_info
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
    model = BuildingWithoutExistingInfrastructure
    form_class = BuildingWithoutExistingInfrastructureEditForm
    template_name = 'projects/edit-project-no-ifr.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_initial(self):
        initial = super().get_initial()
        instance = self.get_object()
        initial.update({
            "name": instance.name,
            "bathroom_sink": instance.bathroom_sink,
            "kitchen_sink": instance.kitchen_sink,
            "toilet_seat": instance.toilet_seat,
            "washing_machine": instance.washing_machine,
            "dishwasher": instance.dishwasher,
            "shower": instance.shower,
            "bathtub": instance.bathtub,
            "building_residence": instance.building_residence,
        })
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context

    def get_success_url(self):
        return reverse("building_no_infrastructure_details", kwargs={"slug_name": self.object.slug, })


class ResidentialBuildingWithInfrastructureEditView(views.UpdateView):
    model = BuildingWithExistingInfrastructure
    form_class = BuildingWithExistingInfrastructureEditForm
    template_name = 'projects/edit-project-with-ifr.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_initial(self):
        initial = super().get_initial()
        instance = self.get_object()
        initial.update({
            "name": instance.name,
            "bathroom_sink": instance.bathroom_sink,
            "kitchen_sink": instance.kitchen_sink,
            "toilet_seat": instance.toilet_seat,
            "washing_machine": instance.washing_machine,
            "dishwasher": instance.dishwasher,
            "shower": instance.shower,
            "bathtub": instance.bathtub,
            "building_residence": instance.building_residence,
            "floor_siphon": instance.floor_siphon,
            "building_area": instance.building_area,
            "property_area": instance.property_area,
            "green_area": instance.green_area,
            "underground_parking_spots": instance.underground_parking_spots,
            "floors": instance.floors,
        })
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context

    def get_success_url(self):
        return reverse("building_with_infrastructure_details", kwargs={"slug_name": self.object.slug, })


class InfrastructureProjectEditView(views.UpdateView):
    model = InfrastructureProject
    form_class = InfrastructureProjectEditForm
    template_name = 'projects/edit-project-infrastructure.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_initial(self):
        initial = super().get_initial()
        instance = self.get_object()
        initial.update({
            'name': instance.name,
            'existing_plumbing_depth': instance.existing_plumbing_depth,
            'new_plumbing_length': instance.new_plumbing_length,
            'new_plumbing_diameter': instance.new_plumbing_diameter,
            'existing_sewer_depth': instance.existing_sewer_depth,
            'new_sewer_length': instance.new_sewer_length,
            'new_sewer_diameter': instance.new_sewer_diameter,
            'existing_pavement': instance.existing_pavement,
        })
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context

    def get_success_url(self):
        return reverse("infrastructure_details", kwargs={"slug_name": self.object.slug, })


class ResidentialBuildingNoInfrastructureDeleteView(views.DeleteView):
    model = BuildingWithoutExistingInfrastructure
    template_name = 'projects/project-details-no-ifr.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'
    success_url = reverse_lazy('my_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class ResidentialBuildingWithInfrastructureDeleteView(views.DeleteView):
    model = BuildingWithExistingInfrastructure
    template_name = 'projects/project-details-with-ifr.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'
    success_url = reverse_lazy('my_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class InfrastructureProjectDeleteView(views.DeleteView):
    model = InfrastructureProject
    template_name = 'projects/project-details-infrastructure.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'
    success_url = reverse_lazy('my_projects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())
