#!/usr/bin/python3
"""
Gets data from API and save all to json
"""
import json
import requests
import sys


def save_all():
    """Fetches all data and dumo to json"""
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/').json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    userss = {}
    dixt = {}

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        for user in users:
            user_id = user.get('id')
            dixt[user_id] = []
            userss[user_id] = user.get('username')

        for task in tasks:
            t = {}
            user_id = task.get('userId')
            t['task'] = task.get('title')
            t['completed'] = task.get('completed')
            t['username'] = userss.get(user_id)
            dixt.get(user_id).append(t)
        json.dump(dixt, f)


if __name__ == "__main__":
    save_all()
