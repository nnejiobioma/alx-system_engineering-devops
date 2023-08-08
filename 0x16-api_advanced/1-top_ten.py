#!/usr/bin/python3
"""
script that queries the Reddit API and returns the number of
subscribers for a given subreddit.
The function should return 0, If an invalid subreddit is given, 
"""
import sys
import json
import requests


hdrs = {
    'User-Agent': 'User-Agent'
}


def top_ten(subreddit):
    """Returns the titles of the first 10 hot posts"""
    try:
        url = 'https://www.reddit.com/r/'
        res = requests.get(url + subreddit + "/hot.json?limit=10",
                                headers=hdrs, allow_redirects=False)
        info = [element['data']['title'] for element in res.
                   json()['data']['children']]
        print(*info, sep='\n')
        # pprint.pprint(res.json())
    except:
        print(None
