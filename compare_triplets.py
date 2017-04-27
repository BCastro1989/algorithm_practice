"""
Date: 4/26/17
Source: Hackerrank
Time: 5-10 minutes

This was a very straight forward problem. I had no trouble thinking
of how to solve it. But I did stop for a second to consider how I
could solve it using a loop instead of 6 if-statements. I decided
on using eval and iterating through the variable names from a0 to
a2 and comparing it to the same iterated values of b0 to b2. This
worked nicely.

The only issue I had is I forgot to use str(n) the first time
around. This caused an error because you can't concatinate str+int.
This could have been avoided by thinking through what I was putting
into eval() a bit more carefully before I tried to run it.

"""


#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a_score = 0
    b_score = 0
    
    for n in xrange(3):
        if eval("a"+str(n)) > eval("b"+str(n)):
            a_score += 1
        elif eval("b"+str(n)) > eval("a"+str(n)):    
            b_score += 1
    return a_score, b_score
            
            
a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))