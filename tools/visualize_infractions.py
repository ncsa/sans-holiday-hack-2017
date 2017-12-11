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
    return m[char]
    n = int(char)
    color_code = COLOR.format(30+n)
    char = " X X X"[n]
    #return color_code + char + END
    return char
    #return ("O" * n) + (" " * (5-n))

def display(line):
    print(''.join(colorify(c) for c in line))

def factor(num):
    return [x for x in range(5, num) if num % x == 0 and num/x > 4]
    
def main():
    with open("infractions.json") as f:
        infractions = json.load(f)

    deduped_infractions = list({v['date']: v for v in infractions}.values())
    # Remove Whos
    if True:
        deduped_infractions = [x for x in deduped_infractions if 'Who' not in x['name']]

    deduped_infractions.sort(key=itemgetter("date"), reverse=True)

    msg = [i['status'] for i in deduped_infractions]

    for cs in factor(len(msg)):
        for chunk in chunks(msg, cs):
            display(chunk)
        print()
        print()
        print()

if __name__ == "__main__":
   main() 
