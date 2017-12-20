#!/usr/bin/env python3
import itertools

import pw

for x in itertools.permutations(pw.words, 2):
    print(' '.join(x))
