import sqlite3
from datetime import datetime
from os import path

""" Refactor note: this class is an exact replica of the class present in {./utils.py}
    This needs to be addressed at a later time, to remove redundancy.
"""


class SQL_queries():
    def __init__(self):
        # return if database already exists
        if path.exists("reports.db"):
            return
        conn = sqlite3.connect("reports.db")
        # create table for storing reports
        conn.execute('''CREATE TABLE REPORT
                    (
                    PROJECT_NAME            TEXT NOT NULL,
                    RUN_ID                  TEXT NOT NULL,
                    TRAINING_START_TIME     TEXT NOT NULL,
                    TRAINING_TIME           TEXT NOT NULL,
                    TESTING_START_TIME      TEXT,
                    TESTING_TIME            TEXT,
                    ACCURACY                INTEGER,
                    UNIQUE(RUN_ID) 
                    );''')
        conn.commit()
        conn.close()

    def add_entry(self, project_name, run_id, training_time_start, training_time, testing_time_start=0, testing_time=0, accuracy=0):
        print("adding the following entry into db:")
        print(project_name, run_id, datetime.fromtimestamp(training_time_start),
              training_time, testing_time_start, testing_time, accuracy)

        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        # database query for inserting row of data into table
        params = (project_name, run_id, datetime.fromtimestamp(
            training_time_start), training_time, testing_time_start, testing_time, accuracy)
        cursor.execute("INSERT INTO REPORT VALUES (?,?,?,?,?,?,?)", params)
        conn.commit()
        conn.close()

        print('db entry added successfully')

    def update_entry(self, run_id, update_params):
        print("updating entry for run_id : {}".format(run_id))

        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()

        # database query for updating row of data from/into table
        cursor.execute('''UPDATE REPORT 
                        SET 
                        TESTING_START_TIME =:TESTING_START_TIME, 
                        TESTING_TIME =:TESTING_TIME, 
                        ACCURACY =:ACCURACY 
                        WHERE 
                        RUN_ID =:RUN_ID ''',
                       {"TESTING_START_TIME": datetime.fromtimestamp(update_params[0]), "TESTING_TIME": update_params[1], "ACCURACY": update_params[2], "RUN_ID": run_id})
        conn.commit()
        conn.close()

        print('db entry updated successfully')

    def retrieve_entry(self, run_id):
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()

        # database query for retrieving data of specific run from table
        cursor.execute(
            "SELECT * FROM REPORT WHERE RUN_ID =:RUN_ID", {"RUN_ID": run_id})
        entry = cursor.fetchone()
        conn.close()
        return entry

    def retrieve_incomplete_entry_run_id(self, project_name):
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()

        # database query for retrieving incomplete data row to be updated later
        cursor.execute("SELECT * FROM REPORT WHERE PROJECT_NAME =:PRJ_NAME AND TESTING_TIME=:ZERO",
                       {"PRJ_NAME": project_name, "ZERO": 0})
        entry = cursor.fetchone()
        conn.close()
        if entry is None:
            print("all trained models are tested")
            exit()
        return entry[1]

    def retrieve_data_for_project(self, project_name):
        # database query for retrieving data for a project
        query = "SELECT * FROM REPORT WHERE PROJECT_NAME = '{}'".format(
            project_name)
        return self.sql_data_to_list_of_dicts(query)

    def retrieve_project_names_and_run_ids(self):
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        # database query for retrieving data(PROJECT_NAME, RUN_ID)
        cursor.execute("SELECT PROJECT_NAME, RUN_ID FROM REPORT")
        entries = cursor.fetchall()
        conn.close()
        return entries

    # this function converts sql data to a list of dicts to be used in a Pythonic way
    def sql_data_to_list_of_dicts(self, query):
        conn = sqlite3.connect('reports.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)
        entries = cursor.fetchall()

        entries_as_list_of_dict = [{k.lower(): item[k] for k in item.keys()}
                                   for item in entries]

        conn.close()
        return entries_as_list_of_dict
