from django.contrib import admin

from wss_app.projects.forms import BuildingWithoutExistingInfrastructureCreateForm, \
    BuildingWithoutExistingInfrastructureEditForm, BuildingWithExistingInfrastructureCreateForm, \
    BuildingWithExistingInfrastructureEditForm, InfrastructureProjectCreateForm, InfrastructureProjectEditForm
from wss_app.projects.models import BuildingWithoutExistingInfrastructure, BuildingWithExistingInfrastructure, \
    InfrastructureProject


@admin.register(BuildingWithoutExistingInfrastructure)
class BuildingWithoutExistingInfrastructureAdmin(admin.ModelAdmin):
    model = BuildingWithoutExistingInfrastructure
    add_form = BuildingWithoutExistingInfrastructureCreateForm
    form = BuildingWithoutExistingInfrastructureEditForm

    list_display = ['name', 'slug', 'project_creator']
    search_fields = ['name', 'project_creator']
    list_filter = ['name', 'project_creator']
    list_per_page = 50
    search_help_text = 'Search by Project Creator and Name'

    fieldsets = (
        (None, {'fields': ('name', 'project_creator')}),
        ('Input info', {'fields': (
            'bathroom_sink', 'kitchen_sink', 'toilet_seat', 'washing_machine', 'dishwasher', 'shower', 'bathtub',
            'building_residence',)}),
    )


@admin.register(BuildingWithExistingInfrastructure)
class BuildingWithExistingInfrastructureAdmin(admin.ModelAdmin):
    model = BuildingWithExistingInfrastructure
    add_form = BuildingWithExistingInfrastructureCreateForm
    form = BuildingWithExistingInfrastructureEditForm

    list_display = ['name', 'slug', 'project_creator']
    search_fields = ['name', 'project_creator']
    list_filter = ['name', 'project_creator']
    list_per_page = 50
    search_help_text = 'Search by Project Creator and Name'

    fieldsets = (
        (None, {'fields': ('name', 'project_creator')}),
        ('Input info', {'fields': (
            'bathroom_sink', 'kitchen_sink', 'toilet_seat', 'washing_machine', 'dishwasher', 'shower', 'bathtub',
            'building_residence', 'floor_siphon', 'building_area', 'property_area', 'green_area',
            'underground_parking_spots', 'floors',)}),
    )


@admin.register(InfrastructureProject)
class InfrastructureProjectAdmin(admin.ModelAdmin):
    model = InfrastructureProject
    add_form = InfrastructureProjectCreateForm
    form = InfrastructureProjectEditForm

    list_display = ['name', 'slug', 'project_creator']
    search_fields = ['name', 'project_creator']
    list_filter = ['name', 'project_creator']
    list_per_page = 50
    search_help_text = 'Search by Project Creator and Name'

    fieldsets = (
        (None, {'fields': ('name', 'project_creator')}),
        ('Input info', {'fields': (
            'existing_plumbing_depth', 'new_plumbing_length', 'new_plumbing_diameter', 'existing_sewer_depth',
            'new_sewer_length', 'new_sewer_diameter', 'settlement_inhabitants', 'existing_pavement')}),

    )
