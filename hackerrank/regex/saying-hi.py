#!/usr/bin/python3
"""
solution to HackerRank's 'Saying Hi' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/saying-hi/problem`
"""

import re

pattern = re.compile(r'^hi\s[^d](.|\n)*$', re.IGNORECASE)

# First line will be number of lines to evaluate
n = int(input())
for _ in range(n):
    line = input()
    match = pattern.search(line)
    if match:
        print(line)
