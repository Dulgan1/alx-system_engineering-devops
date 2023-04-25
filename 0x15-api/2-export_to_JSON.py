#!/usr/bin/python3
"""
    Reads API data and svaes to csv file
"""
import json
import requests
from sys import argv


def save_json():
    """Fetches data and write to csv"""
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': argv[1]}).json()

    for user in users:
        if user.get('id') == int(argv[1]):
            user_name = user.get('username')
            break

    tasks_list = []

    with open('{}.json'.format(argv[1]), 'w', newline='') as f:
        for task in tasks:
            t = {}
            t['task'] = task.get('title')
            t['completed'] = task.get('completed')
            t['username'] = user_name
            tasks_list.append(t)

        dixt = {str(argv[1]) : tasks_list}
        json.dump(dixt, f)



if __name__ == "__main__":
    save_json()
