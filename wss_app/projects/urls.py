from django.urls import path

from wss_app.projects.views import create_project_index, NewResidentialBuildingNoInfrastructureView, \
    NewResidentialBuildingWithInfrastructureView, NewInfrastructureProjectView

urlpatterns = [
    path("", create_project_index, name="create_project_index"),
    path("projects/no_infrastrutcure/", NewResidentialBuildingNoInfrastructureView.as_view(),
         name="build_no_infrastructure"),
    path("projects/with_infrastrutcure/", NewResidentialBuildingWithInfrastructureView.as_view(),
         name="build_with_infrastructure"),
    path("projects/infrastrutcure/", NewInfrastructureProjectView.as_view(),
         name="infrastructure_project"),
]
