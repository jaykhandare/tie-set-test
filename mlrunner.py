import sys
from os import path

import click
from tabulate import tabulate


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

    if not path.exists(script):
        raise FileNotFoundError("script {} does not exist.".format(script))
    if not path.exists(dataset):
        raise FileNotFoundError("dataset {} does not exist.".format(dataset))


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

    if not path.exists(script):
        raise FileNotFoundError("script {} does not exist.".format(script))
    if not path.exists(dataset):
        raise FileNotFoundError("dataset {} does not exist.".format(dataset))


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


if __name__ == "__main__":
    function_name = sys.argv.pop(1)
    if function_name == "train":
        train()
    elif function_name == "test":
        test()
    elif function_name == "report":
        report()
    else:
        print("invalid option")


def test_code():
    pass
