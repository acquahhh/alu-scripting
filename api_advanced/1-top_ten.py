#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    try:
        res = requests.get(url, headers={"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}, params={"limit": 10},
                           allow_redirects=False, timeout=10)
        if res.status_code != 200:
            print(None)
            return
        for child in res.json().get("data", {}).get("children", []):
            print(child.get("data", {}).get("title"))
    except Exception:
        print(None)
