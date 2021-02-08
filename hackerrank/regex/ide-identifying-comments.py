#!/usr/bin/python3
"""
solution to HackerRank's 'Building a Smart IDE: Identifying Comments'
regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/ide-identifying-comments/problem`
"""

import re
from sys import stdin

s = '\n'.join(re.findall(r'(?://.*)|(?:/\*(?:.|\n)*?\*/)', stdin.read()))
print(re.sub(r'\n\s+', '\n', s))
