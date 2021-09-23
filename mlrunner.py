import sys
from os import path
from importlib import import_module

import click
from tabulate import tabulate

from report_generator import Report

@click.command()
@click.option("--project_name", help="name of the project")
@click.option("--script", help="ml script to be used")
@click.option("--learning_rate", help="desired learning rate")
@click.option("--dataset", help="path to dataset")
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
def report(project_name, format, output_path):
    print("starting 'report' module...")
    print()

    table = [("project_name", project_name),
             ("format", format), ("output_path", output_path)]
    print(tabulate(table, headers=["parameter", "value"], tablefmt="github"))
    print()

    reporter = Report()
    print("generating report for project {}".format(project_name))
    reporter.generate_report(project_name)
    print("report generated")

def start_django_ui():
    print("starting django ui...")

if __name__ == "__main__":
    function_name = sys.argv.pop(1)
    if function_name == "train":
        train()
    elif function_name == "test":
        test()
    elif function_name == "report":
        report()
    elif function_name =="ui":
        start_django_ui()
    else:
        print("invalid option")


def test_code():
    pass
