#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: 
{ "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}

File name must be: USER_ID.json
"""
import json
import requests
from sys import argv


def export_to_json():

    user_id = int(argv[1])
    link_user = "https://jsonplaceholder.typicode.com/users/{}"
    link_task = "https://jsonplaceholder.typicode.com/todos"
    employee = requests.get(link_user.format(user_id)).json()
    todos = requests.get(link_task, params={'userId': user_id}).json()
    tasks = []
    wrap_dict = {}
    with open('{}.json'.format(user_id), 'w', newline='') as f:
        for t in todos:
            inner_dict = {}
            inner_dict['task'] = t.get('title')
            inner_dict['completed'] = t.get('completed')
            inner_dict['username'] = employee.get('username')
            tasks.append(inner_dict)
        wrap_dict[user_id] = tasks
        json.dump(wrap_dict, f)


if __name__ == "__main__":
    export_to_json()
