#!/usr/bin/python3
"""
solution to HackerRank's 'Detect HTML Links' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/detect-html-links/problem`
"""

from sys import stdin
import re

regex_sub_strings = [
    r'<a\s+',                     # match 'a' tag opening
    r'(\w[\w-]*?=".*?",*\s*)*?',  # match attr=val pairs before href
    r'href="(?P<link>.*?)",*\s*', # match href attr and capture link
    r'(\w[\w-]*?=".*?",*\s*)*?',  # match attr=val pairs after href
    r'>',                         # match closing of opening tag
    r'(<.*?>)*',                  # match inner tags before text
    r'(?P<text>.*?)',             # match text
    r'(<.*?>)*',                  # match inner tags after text
    r'</a>',                      # match closing tag 
]

def find_links():

    # First line should be number of lines to read. Interpret and validate.
    try:
        N = int(stdin.readline())
        if N <= 0:
            return
    except ValueError:
        print('Bad input')
        exit(1)

    # Use string join method to join all the regex strings into one string.
    regex_string = ''.join(regex_sub_strings)

    # create a re pattern object to compare against input lines
    Pattern = re.compile(regex_string)
    count = 0
    while count < N:
        line = stdin.readline()
        if line is None:
            break
        count += 1
        match = Pattern.search(line)           # find match
        while match:
            link = match.group('link').strip() # extract link, strip whitespace
            text = match.group('text').strip() # extract text, strip whitespace
            print('{},{}'.format(link, text))  # print result

            # find next match, starting off where current match ended
            match = Pattern.search(line, match.end())

    return 0

if __name__ == "__main__":
    find_links()
