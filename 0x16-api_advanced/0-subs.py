#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of  subscribers.
 If an invalid subreddit is given, the function should return 0.
"""
    import requests
    

    def number_of_subscribers(subreddit):
	"""
	Function that returns the number of subscribers
	"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "User-Agent"}
    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code >= 300:
	return res.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
