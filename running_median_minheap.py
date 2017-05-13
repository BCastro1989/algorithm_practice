#!/bin/python

import sys
import bisect as bs


def median(li):
    if len(li)%2 == 0:
        return (li[len(li)/2-1]+li[len(li)/2])/2.0
    else:
        return (li[len(li)/2])/1.0

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    #a.append(a_t)
    bs.insort(a,a_t)
    if len(a) > 0:
        print round(median(a),1)
