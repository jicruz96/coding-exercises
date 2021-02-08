#!/usr/bin/python3
"""
solution to HackerRank's 'Utopian Identification Number' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/utopian-identification-number/problem`
"""

import re

id_pattern_sub_strings = [
    r'^',         # Beginning
    r'[a-z]{,3}', # Must begin with 0-3 lowercase letters
    r'\d{2,8}',   # ... followed by 2 to 8 digits
    r'[A-Z]{3,}', # ... followed by at least 3 uppercase letters
    r'$',         # End
]

id_pattern = re.compile(''.join(id_pattern_sub_strings))

# First line will be number of lines to evaluate
n = int(input())
for _ in range(n):
    if id_pattern.search(id_pattern):
        print('VALID')
    else:
        print('INVALID')
