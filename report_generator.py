from utils import SQL_queries
import json

class Report():
    def __init__(self):
        self.report_save_path = "./reports/"
        self.db_object = SQL_queries()

    def get_all_projects(self):
        projects = self.db_object.retrieve_project_names_and_run_ids()
        return projects

    def generate_report(self, project_name, output_path="./reports", format="json"):
        if format == "json":
            data_as_dict = self.db_object.retrieve_data_for_project(
                project_name)
            with open(self.report_save_path + "{}.json".format(project_name), "w") as outfile:
                json.dump(data_as_dict, outfile)


"""code for testing this classes separately"""
reporter = Report()
reporter.generate_report(reporter.get_all_projects()[0][0])