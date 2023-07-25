#!/usr/bin/python3
"""
    Using what you did in the task #0,
    extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
"""
import json
import requests


def all_to_json():
    """Reads API data and save to .json file"""
    USERS = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """export to json"""
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    all_to_json()
