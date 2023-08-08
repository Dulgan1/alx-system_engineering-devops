#!/usr/bin/python3
""" Requests Reddit API for number of subscribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Alx-Dulgan'})

    if response.status_code == 200:
        data = response.json()
        no_sub = data["data"]["subscribers"]
        return no_sub
    return 0
