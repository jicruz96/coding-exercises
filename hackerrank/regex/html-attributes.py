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
    r'(?P<tag>(?P<name>\w+)',                  # capture tag name
    r'(?:\s+(?:\w+)=("|\').*?\3)*?', # attr, repeated as many times as needed
    r')\s*/?>',                             # end of tag
]
tags = {}
attr_pattern = re.compile(r'(?:\s+(\w+)=(?:"|\').*?(?:"|\'))')
pattern = re.compile(''.join(pattern_sub_strings))
for i in range(n):
    matches = pattern.finditer(input())
    for match in matches:
        name = match.group('name')
        attrs = set(attr_pattern.findall(match.group('tag')))
        if name in tags:
            tags[name].update(attrs)
        else:
            tags[name] = attrs
            
for tag, attrs in sorted(tags.items()):
    print('{}:'.format(tag), end='')
    delim = ''
    for attr in sorted(attrs):
        print('{}{}'.format(delim,attr),end='')
        delim = ','
    print()
