#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of  subscribers.
 If an invalid subreddit is given, the function should return 0.  
"""

    import json
    import requests
    import sys

    header = {"User-Agent": "User-Agent"}
    
    def number_of_subscribers(subreddit):
	"""
	Function that returns the number of subscribers
	""" 

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    response = requests.get(url, headers=hdr, allow_redirects=False)
    if response.status_code >= 300:
	return response.json().get('data', {}).get('subscribers', 0)    
    else:
        return 0

