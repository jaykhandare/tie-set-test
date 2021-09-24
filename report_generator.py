import json

from utils import SQL_queries


# this class is implemented to generate project specific reports to be displayed on django-ui
class Report():
    def __init__(self):
        self.report_save_path = "./reports/"
        self.db_object = SQL_queries()

    def get_all_projects(self):
        projects = self.db_object.retrieve_project_names_and_run_ids()
        return projects

    def generate_report(self, project_name, output_path=None, format="json"):
        if format == "json":
            data_as_dict = self.db_object.retrieve_data_for_project(
                project_name)
            if output_path is None:
                output_path = self.report_save_path
            with open(output_path + "{}.json".format(project_name), "w") as outfile:
                json.dump(data_as_dict, outfile)


"""code for testing this classes separately"""
# reporter = Report()
# reporter.generate_report(reporter.get_all_projects()[0][0])
# reporter.generate_report(reporter.get_all_projects()[2][0])
