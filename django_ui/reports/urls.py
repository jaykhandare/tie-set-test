from django.urls import path

from reports.views import (all_projects, project_view, view_loss_graph_for_run)

urlpatterns = [
    path('all_projects/', all_projects, name="all_projects"),
    path('project_view/', project_view, name="project_view"),
    path('view_loss_graph_for_run/', view_loss_graph_for_run, name="view_loss_graph_for_run"),

]
