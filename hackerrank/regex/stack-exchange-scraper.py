#!/usr/bin/python3
"""
solution to HackerRank's 'Stack Exchange Scraper' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/stack-exchange-scraper/problem`
"""

from sys import stdin
import re

htmlDoc = stdin.read()

groups = ['id', 'question', 'time_asked']

pattern_sub_strings = [
    r'/questions/',              # Beginning (questions url)
    r'(?P<id>\d+)',              # id group
    r'/(.|\n)*?>',               # rest of url and link tag
    r'(?P<question>.*?)',        # question group
    r'<(.|\n)*?',                # rest of HTML content until we hit...
    r'asked\s+<span(.|\n)*?>',   # ... "asked <span.." line, where time is
    r'(?P<time_asked>(.|\n)*?)', # time asked group
    r'<'                         # </span> tag
]

matches = re.finditer(''.join(pattern_sub_strings), htmlDoc)
for match in matches:
    delim = ''
    for group in groups:
        print('{}{}'.format(delim, match.group(group)), end='')
        delim = ';'
    print()
