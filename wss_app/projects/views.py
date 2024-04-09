from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views, View

from wss_app.accounts.views import OwnerRequiredMixin
from wss_app.common.profile_helper import get_profile
from wss_app.projects.calculations import ResidenceBuildingWithoutInfrastructureCalculator, \
    ResidenceBuildingWithInfrastructureCalculator, InfrastructureCalculator
from wss_app.projects.forms import BuildingWithoutExistingInfrastructureCreateForm, \
    BuildingWithExistingInfrastructureCreateForm, InfrastructureProjectCreateForm, \
    BuildingWithoutExistingInfrastructureEditForm, BuildingWithExistingInfrastructureEditForm, \
    InfrastructureProjectEditForm
from wss_app.projects.models import BuildingWithoutExistingInfrastructure, BuildingWithExistingInfrastructure, \
    InfrastructureProject


def create_project_index(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='projects/create-project.html', context=context)


class NewProjectViewMixin(LoginRequiredMixin, views.CreateView):
    template_name = ''
    form_class = None
    model = None
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


class NewResidentialBuildingNoInfrastructureView(NewProjectViewMixin):
    model = BuildingWithoutExistingInfrastructure
    form_class = BuildingWithoutExistingInfrastructureCreateForm
    template_name = 'projects/create-project-no-ifr.html'


class NewResidentialBuildingWithInfrastructureView(NewProjectViewMixin):
    model = BuildingWithExistingInfrastructure
    form_class = BuildingWithExistingInfrastructureCreateForm
    template_name = 'projects/create-project-with-ifr.html'


class NewInfrastructureProjectView(NewProjectViewMixin):
    model = InfrastructureProject
    form_class = InfrastructureProjectCreateForm
    template_name = 'projects/create-project-infrastructure.html'


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
            project.project_type = project.__class__.__name__

        context = {'projects': all_projects, 'user': wss_user}
        return render(request, 'projects/profile-projects.html', context)


class ProjectDetailViewMixin(LoginRequiredMixin, views.DetailView):
    template_name = ''
    model = None
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        building = self.get_object()
        calculator = self.calculator_class(building)
        plumbing_info = calculator.calculate()
        profile = get_profile()
        context['plumbing_info'] = plumbing_info
        context['profile'] = profile
        context['slug'] = self.kwargs.get(self.slug_url_kwarg)
        context['project_name'] = self.object.name if self.object else None
        return context


class ResidentialBuildingNoInfrastructureDetailView(ProjectDetailViewMixin):
    model = BuildingWithoutExistingInfrastructure
    template_name = 'projects/project-details-no-ifr.html'
    calculator_class = ResidenceBuildingWithoutInfrastructureCalculator


class ResidentialBuildingWithInfrastructureDetailView(ProjectDetailViewMixin):
    model = BuildingWithExistingInfrastructure
    template_name = 'projects/project-details-with-ifr.html'
    calculator_class = ResidenceBuildingWithInfrastructureCalculator


class InfrastructureProjectDetailView(ProjectDetailViewMixin):
    model = InfrastructureProject
    template_name = 'projects/project-details-infrastructure.html'
    calculator_class = InfrastructureCalculator


class ProjectEditViewMixin(LoginRequiredMixin, views.UpdateView):
    template_name = ''
    model = None
    form_class = None
    slug_field = 'slug'
    slug_url_kwarg = 'slug_name'

    def get_initial(self):
        initial = super().get_initial()
        instance = self.get_object()
        for field in self.form_class.Meta.fields:
            initial[field] = getattr(instance, field)
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        context['profile'] = profile
        context['project_name'] = self.kwargs.get('name')
        return context

    def get_success_url(self):
        return reverse(self.success_url, kwargs={"slug_name": self.object.slug})


class ResidentialBuildingNoInfrastructureEditView(ProjectEditViewMixin):
    model = BuildingWithoutExistingInfrastructure
    form_class = BuildingWithoutExistingInfrastructureEditForm
    template_name = 'projects/edit-project-no-ifr.html'
    success_url = 'building_no_infrastructure_details'


class ResidentialBuildingWithInfrastructureEditView(ProjectEditViewMixin):
    model = BuildingWithExistingInfrastructure
    form_class = BuildingWithExistingInfrastructureEditForm
    template_name = 'projects/edit-project-with-ifr.html'
    success_url = 'building_with_infrastructure_details'


class InfrastructureProjectEditView(ProjectEditViewMixin):
    model = InfrastructureProject
    form_class = InfrastructureProjectEditForm
    template_name = 'projects/edit-project-infrastructure.html'
    success_url = 'infrastructure_details'


class ProjectDeleteViewMixin(LoginRequiredMixin, views.DeleteView):
    template_name = ''
    model = None
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


class ResidentialBuildingNoInfrastructureDeleteView(ProjectDeleteViewMixin):
    model = BuildingWithoutExistingInfrastructure
    template_name = 'projects/project-details-no-ifr.html'


class ResidentialBuildingWithInfrastructureDeleteView(ProjectDeleteViewMixin):
    model = BuildingWithExistingInfrastructure
    template_name = 'projects/project-details-with-ifr.html'


class InfrastructureProjectDeleteView(ProjectDeleteViewMixin):
    model = InfrastructureProject
    template_name = 'projects/project-details-infrastructure.html'
