#!/usr/bin/python3
"""
solution to HackerRank's 'IP Address Validation' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/ip-address-validation/problem`
"""

import re # Regular expression (regex) Python module

def validate_ip_addresses(ip_addresses):
    """ prints whether a string is a valid IP Address (IPv4 or IPv6) or not """
    IPv4_regex = get_IPv4_regex()
    IPv6_regex = get_IPv6_regex()
    for ip in ip_addresses:
        if re.match(IPv4_regex, ip):
            print('IPv4')
        elif re.match(IPv6_regex, ip):
            print('IPv6')
        else:
            print('Neither')

def get_IPv4_regex():
    """ returns regular expression for valid IPv4 strings """
    return r'^{0}\.{0}\.{0}\.{0}$'.format(get_decimal_8bit_regex())

def get_IPv6_regex():
    """ returns regular expression for valid IPv6 strings """
    hexadecimal_16bit_regex = r'\b[0-9a-f]{1,4}\b'
    return r'^{0}:{0}:{0}:{0}:{0}:{0}:{0}:{0}$'.format(hexadecimal_16bit_regex)

def get_decimal_8bit_regex():
    """ returns regular expression for integers 0, 255, and between"""

    # We construct the regex using a list of sub strings for clarity
    decimal_8bit_regex_sub_strings = [
        r'\b(',               # After a word boundary, num is either...
        r'[1-9]?\d',          # a number between   0 and  99
        r'|',                 # or
        r'1\d{2}',            # a number between 100 and 199
        r'|',                 # or
        r'2(5[0-5]|[0-4]\d)', # a number between 200 and 255
        r')\b',               # ... followed by a word boundary
    ]

    return ''.join(decimal_8bit_regex_sub_strings)


if __name__ == '__main__':

    # First line must be integer equal to number of lines to expect
    with open('file', 'r') as file:
        numLines = int(input())
        lines = []
        while numLines:
            lines.append(input())
            numLines -= 1
        validate_ip_addresses(lines)
