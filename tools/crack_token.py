#!/usr/bin/env python3
import string
from itertools import product
import jwt
import tqdm
import sys

#cookie='xj6oYqq87s996e536780'
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE3LTA4LTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.M7Z4I3CtrWt4SGwfg7mi6V9_4raZE5ehVkI9h04kr6I'

def gen():
    for n in range(1,6):
        print ("Trying:", n)
        for s in product(string.digits+string.lowercase, repeat=n):
            yield ''.join(s)

for w in tqdm.tqdm(gen()):
    try:
        v = jwt.decode(token, w, algorithms=['HS256'])
        print()
        print(w, v)
        print()
        sys.exit(0)
    except jwt.exceptions.DecodeError:
        pass
