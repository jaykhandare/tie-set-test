""" 
    This python script is the first and direct access point to start the program, once the installations are done.
    It implements all the required calls mentioned in the problem statement to be implemented.
"""
import sys
from importlib import import_module
from os import system

import click
from tabulate import tabulate

from report_generator import Report


@click.command()
@click.option("--project_name", help="name of the project")
@click.option("--script", help="ml script to be used")
@click.option("--learning_rate", help="desired learning rate")
@click.option("--dataset", help="path to dataset")
# this method activates the "train" algorithm module
def train(project_name, script, learning_rate, dataset):
    print("starting 'train' module...")
    print()

    table = [("project_name", project_name), ("script", script),
             ("learning_rate", learning_rate), ("dataset", dataset)]
    print(tabulate(table, headers=["parameter", "value"], tablefmt="github"))
    print()

    try:
        ml = import_module(script)
        executioner = ml.ExecuteAlgorithm(project_name)
        executioner.train_algorithm(learning_rate=learning_rate)

    except ImportError as err:
        print("no module exists at {}".format(script))
        print(err)


@click.command()
@click.option("--project_name", help="name of the project")
@click.option("--script", help="ml script to be used")
@click.option("--dataset", help="path to dataset")
# this method activates the "test" algorithm module
def test(project_name, script, dataset):
    print("starting 'test' module...")
    print()

    table = [("project_name", project_name),
             ("script", script), ("dataset", dataset)]
    print(tabulate(table, headers=["parameter", "value"], tablefmt="github"))
    print()

    try:
        ml = import_module(script)
        executioner = ml.ExecuteAlgorithm(project_name)
        executioner.test_algorithm()

    except ImportError as err:
        print("no module exists at {}".format(script))
        print(err)


@click.command()
@click.option("--project_name", help="name of the project")
@click.option("--format", help="desired format of the report")
@click.option("--output_path", help="path to save the report")
# this method activates activates function calls for generating report
def report(project_name, format, output_path):
    print("starting 'report' module...")
    print()

    table = [("project_name", project_name),
             ("format", format), ("output_path", output_path)]
    print(tabulate(table, headers=["parameter", "value"], tablefmt="github"))
    print()

    print("generating report for project {}".format(project_name))
    reporter = Report()
    reporter.generate_report(project_name)
    print("report generated")


# this method activates mechanism to start the django-ui for viewing the reports
def start_django_ui():
    print("starting django ui...")
    bash_command = "echo 'open http://127.0.0.1:8000/all_projects/ in your browser' && python3 django_ui/manage.py runserver"
    system(bash_command)


# __main__ function to call correct function based on the input parameters
if __name__ == "__main__":
    function_name = sys.argv.pop(1)
    if function_name == "train":
        train()
    elif function_name == "test":
        test()
    elif function_name == "report":
        report()
    elif function_name == "ui":
        start_django_ui()
    else:
        print("invalid option")
