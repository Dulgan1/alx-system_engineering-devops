#!/usr/bin/python3
""" Requests Reddit API for titles of 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False,
                            headers={'User-Agent': 'Alx-Dulgan'})

    if response.status_code == 200:
        data = response.json()
        list_d = data["data"]["children"]
        for d in list_d[:10]:
            print(d["data"]["title"])
    else:
        print('None')
