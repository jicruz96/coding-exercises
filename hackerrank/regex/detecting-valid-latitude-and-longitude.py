#!/usr/bin/python3
"""
solution to HackerRank's 'Detecting Valid Latitude and Longitude Pairs'
regex problem

See problem description and input format here:
`https://hackerrank.com/challenges/detecting-valid-latitude-and-longitude/`
"""

import re

numLines = int(input())
latitude = r'(?P<lat>[+-]?' + r'\d{1,2}(?:\.\d+)?' + r')'
longitude = r'(?P<long>[+-]?' r'\d{1,3}(?:\.\d+)?' + r')'
pattern = re.compile(''.join(r'\(' + latitude + r', ' + longitude + r'\)'))
for i in range(numLines):
    match = pattern.match(input())
    if match and abs(float(match.group('lat'))) <= 90 and abs(float(match.group('long'))) <= 180:
        print('Valid')
    else:
        print('Invalid')
