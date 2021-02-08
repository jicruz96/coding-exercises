#!/usr/bin/python3
"""
solution to HackerRank's 'Find HackerRank' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/find-hackerrank/problem`
"""

import re

pattern = re.compile('hackerrank', re.IGNORECASE)
n = int(input())
count = 0
for _ in range(n):
    count += len(pattern.findall(input()))
print(count)
