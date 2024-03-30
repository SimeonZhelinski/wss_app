from django.urls import path, include

from wss_app.projects.views import create_project_index, NewResidentialBuildingNoInfrastructureView, \
    NewResidentialBuildingWithInfrastructureView, NewInfrastructureProjectView, my_projects, \
    ResidentialBuildingNoInfrastructureDetailView, ResidentialBuildingWithInfrastructureDetailView, \
    InfrastructureProjectDetailView, ResidentialBuildingNoInfrastructureEditView, \
    ResidentialBuildingWithInfrastructureEditView, InfrastructureProjectEditView, InfrastructureProjectDeleteView, \
    ResidentialBuildingNoInfrastructureDeleteView, ResidentialBuildingWithInfrastructureDeleteView

urlpatterns = [
    path("", create_project_index, name="create_project_index"),
    path("projects/no_infrastrutcure/",
         NewResidentialBuildingNoInfrastructureView.as_view(),
         name="build_no_infrastructure"),
    path("projects/with_infrastrutcure/",
         NewResidentialBuildingWithInfrastructureView.as_view(),
         name="build_with_infrastructure"),
    path("projects/infrastrutcure/",
         NewInfrastructureProjectView.as_view(),
         name="infrastructure_project"),
    path("projects/my-projects/", my_projects, name="my_projects"),

    path("projects/no_infrastrutcure/<slug:slug_name>/",
         include([
             path("", ResidentialBuildingNoInfrastructureDetailView.as_view(),
                  name="building_no_infrastructure_details"),
             path("edit/", ResidentialBuildingNoInfrastructureEditView.as_view(),
                  name="building_no_infrastructure_edit"),
             path("delete/", ResidentialBuildingNoInfrastructureDeleteView.as_view(),
                  name="building_no_infrastructure_delete")

         ])
         ),

    path("projects/with_infrastrutcure/<slug:slug_name>/",
         include([
             path("", ResidentialBuildingWithInfrastructureDetailView.as_view(),
                  name="building_with_infrastructure_details"),
             path("edit/", ResidentialBuildingWithInfrastructureEditView.as_view(),
                  name="building_with_infrastructure_edit"),
             path("delete/", ResidentialBuildingWithInfrastructureDeleteView.as_view(),
                  name="building_with_infrastructure_delete")

         ])
         ),

    path("projects/infrastrutcure/<slug:slug_name>/",
         include([
             path("", InfrastructureProjectDetailView.as_view(),
                  name="infrastructure_details"),
             path("edit/", InfrastructureProjectEditView.as_view(),
                  name="infrastructure_edit"),
             path("delete/", InfrastructureProjectDeleteView.as_view(),
                  name="infrastructure_delete")

         ])
         )
]
