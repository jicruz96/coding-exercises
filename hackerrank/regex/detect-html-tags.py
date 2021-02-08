#!/usr/bin/python3
"""
solution to HackerRank's 'Detect HTML Attributes' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/html-attributes/problem`
"""
import re

n = int(input())
pattern_sub_strings = [
    r'<',                             # opening of a tag
    r'(?P<tag>\w+)',                  # capture tag name
    r'(?:\s+(?:\w+)=("|\').*?\2)*?', # attr, repeated as many times as needed
    r'\s*/?>',                             # end of tag
]
pattern = re.compile(''.join(pattern_sub_strings))
tags = set()
for i in range(n):
    matches = pattern.finditer(input())
    for match in matches:
        tags.add(match.group('tag'))
delim = ''
for tag in sorted(tags):
    print('{}{}'.format(delim, tag),end='')
    delim = ';'
print()
