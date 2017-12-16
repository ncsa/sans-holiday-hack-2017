#!/usr/bin/env python3
import json
from operator import itemgetter
from collections import defaultdict

WANT = set(['Aggravated pulling of hair', 'Throwing rocks (at people)', 'Throwing rocks (non-person target)'])

def main():
    byname = defaultdict(set)
    with open("../output/infractions.json") as f:
        infractions = json.load(f)

    for i in infractions:
        byname[i['name']].add(i['title'])

    for n, titles in byname.items():
        if len(titles & WANT) > 1:
            print(n,titles)

if __name__ == "__main__":
   main() 
