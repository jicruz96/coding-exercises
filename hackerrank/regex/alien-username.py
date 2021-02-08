#!/usr/bin/python3
"""
Script that prints if a username read from stdin is valid.

Task Description in Full:
`https://www.hackerrank.com/challenges/alien-username/problem`
"""

import re # regular expressions (regex) Python module

# We construct the regex string from a list of sub-strings for clarity.
valid_pattern_sub_strings = [
    r'^[_.]',     # First character must be either an underscore or period
    r'\d+',       # First character must be followed by one or more digits
    r'[a-zA-Z]*', # Digits must be followed by zero or more letters
    r'_?$'        # String must end with digit or optional underscore
]

def validate_usernames(usernames, valid_pattern):
    """
    method that prints, in order, if a username in a list of usernames is valid
    """
    
    for username in usernames:
        if re.match(valid_pattern, username):
            print('VALID')
        else:
            print('INVALID')
    

if __name__ == '__main__':

    num_usernames = int(input())
    usernames = []
    while num_usernames:
            usernames.append(input())
            num_usernames -= 1
    valid_pattern = ''.join(valid_pattern_sub_strings)
    validate_usernames(usernames, valid_pattern)
