"""
Date: 4/27/17
Source: Hackerrank & Cracking the Coding Interview
Time: 5 min

This was one of those problems that was so simple I had to try not to think too
much. I was trying to find ways to modify the array in place, but realized that
doing so would likley require a more complicated algorithm than nessecary. So
I opted just for generating a new array, appending the new values using the
offset. This runs in O(n) time and O(n) space.

After completing it, and looking at other's solutions, I found an even better
solution I wish I had thought of. Index slicing! Python allows you to generate a
new list from portions of an old one. No loops nessecary, just:

return a[k:] + a[:k]

Which will return all elems from k to end, and append elems from 0 to k.
Note that this is the same exact time complexity. It's just a bit more
neat/pythonic. I believe the space complexity is also the same, but not sure.

"""


def array_left_rotation(a, n, k):
    b = []
    for i in xrange(0,n):
        b.append(a[(i+k)%n])
    return b

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
