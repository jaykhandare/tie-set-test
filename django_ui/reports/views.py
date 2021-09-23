from django.http.response import Http404
from django.shortcuts import render

from os import path


# Create your views here.
def all_projects(request):
    retrieve_all_projects()
    if request.method == "GET":
        return render(request,)
    else:
        return render(request, Http404)


def project_view(request):
    if request.method == "GET":
        return render(request, )
    else:
        return render(request, Http404)

def retrieve_all_projects():
    base_project_dir = "../"
    report_dir_location = base_project_dir + "reports/"
    # loss_dir_location = base_project_dir + "loss_files/"
    print("reports being retrieved...")

    # print(path.abspath(report_dir_location))
    # print(path.abspath(loss_dir_location))

    if not path.exists(report_dir_location):
        print("error while retrieving reports, no reports found")
        return None
    
    # retrieve file data from report_dir_location and send curated data back






def retrieve_report_for_project(project_name):
    base_project_dir = "../"
    report_dir_location = base_project_dir + "reports/"

    # return all data for specific project from report_dir_location


def retrieve_loss_value_files_for_project(project_name):
    base_project_dir = "../"
    loss_dir_location = base_project_dir + "loss_files/"

    # return loss values for generating graph for each run from loss_dir_location
    pass
