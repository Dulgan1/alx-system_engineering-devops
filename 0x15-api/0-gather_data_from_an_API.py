#!/usr/bin/python3
"""
    Reads data from API:
    Gets users data,  match user with passed id (cmdline argument)
    and gets the user's task data
"""
import requests
from sys import argv


def run_all():
    """Fetches data and display"""
    todo_link = "http://jsonplaceholder.typicode.com/todos"
    users = requests.get("http://jsonplaceholder.typicode.com/users/").json()

    for user in users:
        if user.get('id') == int(argv[1]):
            employee = user.get('name')
            break
    num_done_tasks = 0
    total_num_tasks = 0
    tasks_list = []
    tasks_todo = requests.get(todo_link).json()

    for task in tasks_todo:
        if task.get('userId') == int(argv[1]):
            total_num_tasks += 1
            if task.get('completed') is True:
                num_done_tasks += 1
                tasks_list.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          num_done_tasks,
                                                          total_num_tasks))
    for task in tasks_list:
        print("\t {}".format(task))


if __name__ == "__main__":
    run_all()
