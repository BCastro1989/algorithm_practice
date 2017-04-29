'''
Date: 4/19/17
Source: Hackerrank - CTCI
Time: 30 min, but really less than 10 of actual work because I was listening to
    Wait Wait Don't Tell Me while completing it.

Fairly straightforward problem, but I am not fully content with my solution as
it has 4 for loops. Although still constant time (no nested loops), I feel it
should be manageable to do with less loops.

Other solutions replace the first loop with a line that automatically generates
a dict of 26 elems and sets them equal to zero, and one used a neat method I
was unaware of, collections.Counter

from collections import Counter
def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())

'''


def number_needed(a, b):
    occurances = {}

    for c in a+b:
        occurances[c] = 0
    for c in a:
        occurances[c] += 1
    for c in b:
        occurances[c] -= 1

    changes = 0
    for c in occurances:
        changes += abs(occurances[c])
    return changes

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
