#!/usr/bin/python3
"""Requests Reddit API for hot articles in subreddit and keep
count of keywords
"""

import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """Request subreddit recursively
    """
    if not count_list:
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                    'count': 0}))

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if next_page:
        url += '?after={}'.format(next_page)

    res = requests.get(url, allow_redirects=False,
                     headers={"User-Agent": "Alx-Dulgan"})

    if res.status_code != 200:
        return

    data = res.json()['data']

    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']), reverse=True)
        keywords_matched = 0
        for word in sorted_list:
            if word['count'] > 0:
                print('{}: {}'.format(word['keyword'], word['count']))
                keywords_matched += 1
        return
