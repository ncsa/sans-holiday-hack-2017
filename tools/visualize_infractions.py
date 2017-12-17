#!/usr/bin/env python3
import csv
import json
from operator import itemgetter
from collections import defaultdict

WANT = set(['Aggravated pulling of hair', 'Throwing rocks (at people)', 'Throwing rocks (non-person target)'])

def get_naughty():
    with open("../support_files/FileStore/Naughty and Nice List.csv") as f:
        reader = csv.reader(f)
        rows = list(reader)

    return [name for (name, naughty) in rows if naughty == 'Naughty']

def main():
    byname = defaultdict(set)
    infraction_count_byname = defaultdict(int)
    with open("../output/infractions.json") as f:
        infractions = json.load(f)

    for i in infractions:
        byname[i['name']].add(i['title'])
        infraction_count_byname[i['name']] += 1

    print("Six insider threat moles:")
    for n, titles in byname.items():
        if len(titles & WANT) >= 2:
            print("*", n,titles)

    #############

    min_infractions = min(infraction_count_byname[name] for name in get_naughty())

    print()
    print("How many infractions are required to be marked as naughty on Santa's Naughty and Nice List:", min_infractions)

if __name__ == "__main__":
   main() 
