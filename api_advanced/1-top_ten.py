#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/acquahhh)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        children = response.json().get("data", {}).get("children", [])
        for child in children[:10]:
            print(child.get("data", {}).get("title"))
    except Exception:
        print(None)
