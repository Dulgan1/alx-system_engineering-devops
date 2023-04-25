#!/usr/bin/python3
"""
    Reads API data and svaes to csv file
"""
import csv
import requests
from sys import argv


def save_csv():
    users = requests.get("http://jsonplaceholder.typicode.com/users").json
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': argv[1]}).json()

    for user in users:
        if user.get('id') == int(argv[1]):
            user_name = user.get('username')
            break

    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        write_to = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            write_to.writerow([argv[1], user_name, task.get('comoleted'),
                              task.get('title')])
