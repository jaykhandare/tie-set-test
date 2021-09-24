from django.shortcuts import render

from django_ui.template_declarations import *
import os, os.path
import json
import csv

base_project_dir = "../"
report_dir_location = base_project_dir + "reports/"
loss_dir_location = base_project_dir + "loss_files/"

# Create your views here.
def all_projects(request):
    if request.method == "GET":
        projects = retrieve_all_projects()
        projects = [ file.split(".")[0] for file in projects ]
        return render(request, PROJECTS, {"data" : sorted(projects)})
    else:
        return render(request, ERROR_404)

def project_view(request):
    if request.method == "GET":
        project_name = request.GET['project_name']
        print("project view being retrieved for project {}".format(project_name))
        # retrieve json data for selected project
        json_file_path = report_dir_location + project_name + ".json"
        if not os.path.exists(json_file_path):
            return render(request, ERROR_403)
        
        with open(json_file_path, "r") as f:
            data = json.load(f)
        # print(data)
        headers = ["run_id", "training_start_time", "training_time", "testing_start_time", "testing_time", "accuracy", "loss_graph"]
        return render(request, PROJECT_REPORT, {"data" : data, "headers" : headers})
    else:
        return render(request, ERROR_404)

def view_loss_graph_for_run(request):
    if request.method == "GET":
        run_id = request.GET['run_id']
        print("loss value graph being retrieved for run_id {}".format(run_id))
        # retrieve loss item data for selected run
        loss_file_path = loss_dir_location + run_id + ".csv"
        print(loss_file_path)
        if not os.path.exists(loss_file_path):
            return render(request, ERROR_500)

        with open(loss_file_path, "r") as file:
            csv_reader = csv.reader(file)
            data_for_loss_graph = list(csv_reader)
        print(data_for_loss_graph[0])

        return render(request, PROJECT_REPORT)
    else:
        return render(request, ERROR_404)


def retrieve_all_projects():
    print("reports being retrieved...")
    # retrieve file data from report_dir_location and send curated data back
    file_list = os.listdir(report_dir_location)
    print("project names retrieved: ", file_list)
    return file_list


def retrieve_loss_value_files_for_project(project_name):
    base_project_dir = "../"

    # return loss values for generating graph for each run from loss_dir_location
    pass
