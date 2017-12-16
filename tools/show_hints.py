#!/usr/bin/env python3
import collections
import json
import sys

filename = sys.argv[1]

with open(filename) as f:
    data = json.load(f)

tokens = data['mytokens']

all_hints = collections.defaultdict(list)

for t in tokens:
    hints = [m for m in t['metadata'] if m['type'] == 'hint']
    for h in hints:
        all_hints[h['name']].append(h)

for name, hints in all_hints.items():
    print(name)
    print("=" * 20)
    for h in hints:
        print("1.", h['body'])
    print()
