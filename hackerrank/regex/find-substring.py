#!/usr/bin/python3
"""
solution to HackerRank's 'Find Substring' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/find-substring/problem`
"""

import re

numLines = int(input())
lines = ''
for _ in range(numLines):
    lines += input() + ' '
    numLines -= 1
numWords = int(input())
for _ in range(numWords): 
    print(len(re.findall(r'\w' + input() + r'\w', lines)))
