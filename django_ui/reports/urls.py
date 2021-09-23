from django.urls import path

from reports.views import (all_projects, project_view)

urlpatterns = [
    path('all_projects/', all_projects, name="all_projects"),
    path('project_view/', project_view, name="project_view"),

]
