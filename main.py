#!/usr/bin/env python3
"""
Project Name: github-latest
File Name: main.py
Author: Travis Brackney
Class: Python 230 - Self paced online
Date Created 10/6/2019
Python Version: 3.7.2
"""


import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)


def get_event_time(username):
    base_url = "https://api.github.com/"
    events_url = f"{base_url}users/{username}/events"

    response = requests.get(events_url)
    parsed = json.loads(response.text)
    return parsed[0]['created_at']


if __name__ == "__main__":
    username = sys.argv[1]

    # Done:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    timestamp = get_event_time(username)

    print(timestamp)
