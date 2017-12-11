#!/usr/bin/env python3
import requests
import json

BASE = "http://nppd.northpolechristmastown.com/"

def search_infractions(query):
    url = BASE + "infractions"

    params = {
        "json": "1",
        "query": query,
    }
    resp = requests.get(url, params=params).json()
    return resp['infractions']


def download_infractions():
    old = search_infractions("date <= 2017-12-10")
    recent = search_infractions("date > 2017-12-10")
    all_infractions = old+recent

    print("Old infractions", len(old))
    print("Recent infractions", len(recent))
    print("Total infractions", len(all_infractions))

    with open("infractions.json", 'w') as f:
        json.dump(all_infractions, f, indent=4)

if __name__ == "__main__":
    download_infractions()
