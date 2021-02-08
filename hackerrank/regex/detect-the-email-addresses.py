#!/usr/bin/python3
"""
solution to HackerRank's 'Detect the Email Addresses' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/detect-the-email-addresses/problem`
"""

import re

emails = set()
numLines = int(input())
for i in range(numLines):
    emails.update(re.findall(r"\b(?:\w+\.)*\w+\@\w+(?:\.\w+)+\b", input()))
print(';'.join(sorted(emails)))
