#!/usr/bin/env python3
import binascii
import os
import zlib
import base64

with open("../output/humans.txt") as f:
    txt = f.read()

#grab just the last paragraph
txt = txt.split("\n\n")[-1]

s = txt.replace("\n", "").strip()
decoded = binascii.unhexlify(s)

with open("humans.dat", 'wb') as f:
    f.write(decoded)

os.system("file humans.dat")

decompressed = zlib.decompress(decoded)
result = base64.decodestring(decompressed).decode('ascii')

print(result)

card = result.splitlines()
lines = [line[3:-2:2] for line in card]
lines = [line for line in lines if line.strip() and '_' not in line]

def convert(line):
    return ''.join('1' if c == '#' else '0' for c in line)

with open("punchcard.txt", 'w') as f:
    for line in lines:
        l = (convert(line));
        f.write(l)
