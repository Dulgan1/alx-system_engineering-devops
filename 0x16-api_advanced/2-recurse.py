#!/usr/bin/python3
"""Requests from Reddit API, the titles of hot articles in a
subreddit"""

import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """Recursive function to achieve request goal
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if next_page:
        url += '?after={}'.format(next_page)

    response = requests.get(url, allow_redirects=False,
                            headers={"User-Agent": "Alx-Dulgan"})

    if response.status_code == 200:
        data = response.json()['data']
        list_d = data['children']
        for post in list_d:
            count += 1
            hot_list.append(post['data']['title'])
        next_page = data['after']
        if next_page is not None:
            return recurse(subreddit, hot_list, next_page, count)
        else:
            return hot_list
    else:
        return None
