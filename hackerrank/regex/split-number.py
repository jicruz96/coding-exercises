#!/usr/bin/python3
"""
solution to HackerRank's 'Split Number' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/split-number/problem`
"""

import re


# groups list, to be used to create regex string and to summon values
groups = ['CountryCode', 'LocalAreaCode', 'Number']

# Build regex string using list-- for clarity
pattern_sub_strings = [
    r'^',                            # Beginning
    r'(?P<%s>\d{1,3})' % groups[0],  # CountryCode (1 to 3 digits)
    r'([- ])',                       # separator (dash or space)
    r'(?P<%s>\d{1,3})' % groups[1],  # LocalAreaCode (1 to 3 digits)
    r'(\2)',                         # separator (repeat previous)
    r'(?P<%s>\d{4,10})' % groups[2], # Number (4 to 10 digits)
    r'$'                             # End
]

# Create regex pattern object from string (use join method to create string)
pattern = re.compile(''.join(pattern_sub_strings))

# Inspect n lines (n is first line of input)
n = int(input())
for _ in range(n):
    match = pattern.match(input())
    if match:
        delim = ''
        for group in groups:
            print('{}{}={}'.format(delim, group, match.group(group)), end='')
            delim = ','
        print()
