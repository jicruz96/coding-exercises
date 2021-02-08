#!/usr/bin/python3
"""
solution to HackerRank's 'Detect the Domain Name' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/detect-the-domain-name/problem`
"""

import re

domains = set()
numLines = int(input())
pattern_sub_strings = [
    r'(?:https?:\/\/)',
    r'(?:ww[w2]\.)?',
    r'([\da-zA-Z\-]+(?:\.[\da-zA-Z\-]+)+)'
]
pattern = ''.join(pattern_sub_strings)
for i in range(numLines):
    domains.update(re.findall(pattern, input()))
print('\n'.join(sorted(domains)))
