#!/usr/bin/python3
"""
    Write a Python script that, using this REST API,
    for a given employee ID, returns information about
    his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter,
which is the employee ID
The script must display on the standard output the employee
TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks,
which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import requests
from sys import argv


def read_display_data():
    """Reads and displays API data"""
    user_id = int(argv[1])
    link = "http://jsonplaceholder.typicode.com/users/{}"
    user = requests.get(link.format(user_id)).json()
    user_name = user.get('name')
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == user_id:
            TOTAL_NUM_OF_TASKS += 1
            if t.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(t.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
          user_name, NUMBER_OF_DONE_TASKS,
          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    read_display_data()
