#!/usr/bin/python3
"""
    Using what you did in the task #0,
    extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv


def to_csv():
    """ Read amd write API data to CSV"""
    user_id = int(argv[1])
    link_user = "https://jsonplaceholder.typicode.com/users/{}"
    link_task = "https://jsonplaceholder.typicode.com/todos"
    employee = requests.get(link_user.format(user_id)).json()
    todos = requests.get(link_task, params={'userId': user_id}).json()

    employee_name = employee.get('name')

    with open('{}.csv'.format(user_id), 'w', newline='') as f:
        writer_to_csv = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer_to_csv.writerow([user_id, employee.get(
                'username'), task.get('completed'), task.get('title')])


if __name__ == "__main__":
    to_csv()
