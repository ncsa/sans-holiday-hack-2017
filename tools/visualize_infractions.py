#!/usr/bin/env python3
import json
from operator import itemgetter


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

m = {
    'closed': 'O',
    'pending': '.',
    'open': ' ',
}

COLOR = '\033[{}m'
END = '\033[0m'
def colorify(char):
    #return m[n]
    n = int(char)
    color_code = COLOR.format(30+n)
    char = " O X ."[n]
    return color_code + char + END
    #return ("O" * n) + (" " * (5-n))

def display(line):
    print(''.join(colorify(c) for c in line))

def main():
    with open("infractions.json") as f:
        infractions = json.load(f)

    infractions.sort(key=itemgetter("date"), reverse=True)

    msg = [int(i['severity']) for i in infractions]

    for cs in range(5,220):
        for chunk in chunks(msg, cs):
            display(chunk)
        print()
        print()
        print()

if __name__ == "__main__":
   main() 
