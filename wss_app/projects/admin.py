from django.contrib import admin

from wss_app.projects.models import BuildingWithoutExistingInfrastructure, BuildingWithExistingInfrastructure, \
    InfrastructureProject


@admin.register(BuildingWithoutExistingInfrastructure)
class BuildingWithoutExistingInfrastructureAdmin(admin.ModelAdmin):
    pass


@admin.register(BuildingWithExistingInfrastructure)
class BuildingWithExistingInfrastructureAdmin(admin.ModelAdmin):
    pass


@admin.register(InfrastructureProject)
class InfrastructureProjectAdmin(admin.ModelAdmin):
    pass