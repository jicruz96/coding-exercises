#!/usr/bin/python3
"""
finds frequency of a word, counting both UK & US versions word
(e.g. 'color' vs 'colour', 'favorite' vs 'favourite')

Task Description in Full:
`https://www.hackerrank.com/challenges/uk-and-us-2/problem`
"""

import re

# First line of input is number of lines of text. Grab and convert value.
numLines = int(input())

# Store lines of text in `text` string.
text = ''
for i in range(numLines):
    text +=  input() + '\n' # input() trims out the newline. add it back.

# Next line of input is number of test words. Grab and convert value
numLines = int(input())
for i in range(numLines):

    # get word
    word = input()

    # create regex string that finds both UK/US versions of word
    """
    regex_string value explanation:

    Take 'colour', for example. If we want to match both 'color' and
    'colour', we can we can use: 'colou?r'.
    
    The '?' before the 'u' means "there must be one 'u' or zero 'u's".
    
    This will match both 'color' and 'colour'.

    BUT it also will match 'technicolor' and 'colorful', so we add word
    boundaries ('\b') to either side of the word to complete the regex string.
    """ 
    regex_string = r'\b' + word.replace('our', 'ou?r') + r'\b'

    # find all matches
    matches = re.findall(regex_string, text)

    # count matches
    numMatches = len(matches)

    # print matches
    print(numMatches)
