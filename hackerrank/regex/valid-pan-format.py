#!/usr/bin/python3
"""
solution to HackerRank's 'Valid PAN Format' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/valid-pan-format/problem`
"""

import re

pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]$')

# First line will be number of lines to evaluate
n = int(input())
for _ in range(n):
    if pattern.fullmatch(input()):
        print('YES')
    else:
        print('NO')
