#!/usr/bin/python3
"""
solution to HackerRank's 'HackerRank Language' regex problem

See problem description and input format here:
`https://www.hackerrank.com/challenges/hackerrank-language/problem`
"""
import re


languages = [ 'C','CPP','JAVA','PYTHON','PERL','PHP','RUBY','CSHARP','HASKELL',
'CLOJURE','BASH','SCALA','ERLANG','CLISP','LUA','BRAINFUCK','JAVASCRIPT','GO',
'D','OCAML','R','PASCAL','SBCL','DART','GROOVY','OBJECTIVEC'
]

pattern = re.compile(r'\d{5}\s(?P<language>[A-Z]*)')
n = int(input())
for _ in range(n):
    line = input()
    if pattern.match(line).group('language') in languages:
        print('VALID')
    else:
        print('INVALID')
