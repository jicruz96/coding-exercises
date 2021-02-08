#!/usr/bin/python3
"""
solution to HackerRank's 'Find a Word' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/find-a-word/problem`
"""

import re

numLines = int(input())
lines = ''
while numLines:
    lines += input() + ' '
    numLines -= 1
numWords = int(input())
while numWords: 
    print(len(re.findall(r'\b' + input() + r'\b', lines)))
    numWords -= 1
