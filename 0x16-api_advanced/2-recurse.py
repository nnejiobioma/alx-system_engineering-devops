#!/usr/bin/python3
"""
script that queries the Reddit API and ouput the titles of
a given subredit. If no results are found for
the given subreddit, the function should return None.
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return the first 10 hot posts listed for a given subreddit."""
    if after is not "":
        URL = "https://www.reddit.com/r/{}/hot/.json?after={}".format(
            subreddit, after)
    else:
        URL = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/51.0.2704.103'}
    info = requests.get(URL, headers=headers)
    if info.status_code == 200:
        info = info.json()
        get = info.get('data').get('children')
        after = info.get('data').get('after')
        for list in get:
            my_y = list.get("data").get("title")
            hot_list.append(my_y)
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
