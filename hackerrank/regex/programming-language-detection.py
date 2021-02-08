#!/usr/bin/python3
"""
solution to HackerRank's 'Programming Language Detection' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/programming-language-detection/problem`
"""

import re
from sys import stdin

text = stdin.read()

if '#include' in text:
    print('C')
elif re.search('import.*?;\s*\n', text):
    print('Java')
else:
    print('Python')
