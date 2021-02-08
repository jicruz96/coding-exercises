#!/usr/bin/python3
"""
solution to HackerRank's 'HackerRank Tweets' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/hackerrank-tweets/problem`
"""

import re

word = 'hackerrank'
at_end = re.compile(word + '$')
at_start = re.compile('^' + word)
n = int(input())
for _ in range(n):
    conversation = input()
    if at_start.search(conversation):
        if at_end.search(conversation):
            print(0)
        else:
            print(1)
    elif at_end.search(conversation):
        print(2)
    else:
        print(-1)
