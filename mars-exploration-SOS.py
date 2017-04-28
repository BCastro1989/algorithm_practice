"""
Date 4/26/17
Source: Hackerrank
Time: 5-10 min

My first thought was to solve it the way I did, using sequential 
if statements. However I took some time to consider other
approaches, hoping Id find a function similar to zip() but that
instead of terminating after the end of the shorter of two lists,
would just repeat one to be the same legth
Ex: zip_repeat("abcdefg","123") -> a,1 b,2 c,3 d,1 e,2 f,3 g,1 etc

I could not find any easy build in function to do this, so I just
went with my original plan. Not as verbose as I thought it might be
in part beause the letter S appears twice and can fit in one if

Mistakes made:
1. forgot a colon after an if statement, silly syntax error
2. thought that all letters came in as lowercase, not uppercase, 
so it failed the first time since it never matched case

These mistakes could be avoided by re-reading the question and 
looking for obvious syntax errors before submitting 
"""


#!/bin/python

import sys


S = raw_input().strip()
msg = "sos"
errors = 0

for i, c in enumerate(S):
    if i%3 == 0 or i%3 == 2:
        if c != "S":
            errors += 1
    else: # i%3 == 1
        if c != "O":
            errors += 1

print errors