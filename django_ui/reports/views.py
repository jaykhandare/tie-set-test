import csv
import json
import os
import os.path
from math import floor

from django.shortcuts import render
from django_ui.template_declarations import *
from plotly.graph_objs import Scatter
from plotly.offline import plot

base_project_dir = "./"
report_dir_location = base_project_dir + "reports/"
loss_dir_location = base_project_dir + "loss_files/"


# this is the current landing page which shows all the projects which are run with the program
def all_projects(request):
    if request.method == "GET":
        projects = retrieve_all_projects()
        projects = [file.split(".")[0] for file in projects]
        return render(request, PROJECTS, {"data": sorted(projects)})
    else:
        return render(request, ERROR_404)


# this view provides project specific information like details of various runs, etc
def project_view(request):
    if request.method == "GET":
        project_name = request.GET['project_name']
        print("project view being retrieved for project {}".format(project_name))

        # retrieve json data file for selected project
        json_file_path = report_dir_location + project_name + ".json"
        if not os.path.exists(json_file_path):
            return render(request, ERROR_403)

        with open(json_file_path, "r") as f:
            data = json.load(f)
        headers = ["run_id", "training_start_time", "training_time",
                   "testing_start_time", "testing_time", "accuracy", "loss_graph"]
        return render(request, PROJECT_REPORT, {"data": data, "headers": headers})
    else:
        return render(request, ERROR_404)


# this view is called from project view with run_id to show the loss items graph
def view_loss_graph_for_run(request):
    if request.method == "GET":
        run_id = request.GET['run_id']
        print("loss value graph being retrieved for run_id {}".format(run_id))

        # retrieve loss item data for selected run
        loss_file_path = loss_dir_location + run_id + ".csv"
        if not os.path.exists(loss_file_path):
            return render(request, ERROR_500)

        with open(loss_file_path, "r") as file:
            csv_reader = csv.reader(file)
            data_for_loss_graph = list(csv_reader)[0]

        # covert loss items data into percentage to show efficiently in a graph
        data_for_loss_graph = [floor(float(entry) * 100)
                               for entry in data_for_loss_graph]

        # list of numbers to the size of loss items
        points_for_x = [x+1 for x in range(len(data_for_loss_graph))]

        layout = {
            'title': run_id,
            'xaxis_title': 'Epochs',
            'yaxis_title': 'Loss function values in percentage',
            'height': 720,
            'width': 1080,
        }

        graph = [Scatter(x=points_for_x, y=data_for_loss_graph,
                         mode='lines+markers', name=run_id)]
        plot_div = plot({'data': graph, 'layout': layout}, output_type='div')

        return render(request, LOSS_GRAPH_VIEW, {'plot_div': plot_div})
    else:
        return render(request, ERROR_404)


# this function is called internally from the methods of THIS SCRIPT ONLY
def retrieve_all_projects():
    print("reports being retrieved...")
    # retrieve file data from report_dir_location and send curated data back
    print(os.listdir("."))
    file_list = os.listdir(report_dir_location)
    print("project names retrieved: ", file_list)
    return file_list
