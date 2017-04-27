"""
Date 4/26/17
Source: Hackerrank
Time: 10-15 min

Fairly easy/Straight forward problem. Took a little bit of time to
follow what the pre-written for loop was doing, but once I saw it
create a 2D array a, the rest became easy

Had one minor problem/mistake. I forgot that n = len, which is one
more than the largest index, so using n - i gave an index out of
bounds issue. Could have been avoided by taking my time when
answering the question of by reading over code more quickly before
pressing run.
"""


#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

diag1 = 0
diag2 = 0
for i in xrange(n):
    diag1 += a[i][i]
    diag2 += a[i][n-1-i]
    
print abs(diag1 - diag2)