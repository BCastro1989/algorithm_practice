'''
DATE: 4/25/16
Source: Codility

This problem was not hard, but there were a few gotchas! that caused me to take
 three tries to get it right.

1. Although I understood the question, I quickly forgot an important detail when
 coding the solution. I had forgotten that a gap is defined as being between
 1's, and I decided to look for just the longest string of zeros. I actually
 wrote an extra line of code, max(bin_gaps, max_gaps) specifically to grab
 trailing zeros, which we do NOT want, since trailing zeros are not bounded by
 1. This was easily fixed by removing that line of code

2. In the speficic case of n=1, the binary representation is 1, so there are no
 zeros. However, since 1/2 = 0 (python does a floor on all division) and then my
 function appends the remainder to that value (1), I ended up getting a result
 of "01" from the input "1", which has a leading zero. This was easily fixed by
 casting to an int and back: bin_string = str(int(bin_string))

Both of these issues could have been avoided if I had made sure to read the
question more carefully AFTER I wrote a solution (I knew what it said, just
forgot as I wrote the code), and by looking more closely at the output from test
cases (I had seen "01", with the result "1", and thought that it was correct
because there was one zero). Overall it pays to pay attention!

I was given 2 hours for this task, and completed it in about 30 minutes.
'''



# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    divides = N/2
    remain = N%2

    def helper(N):
        if N < 2:
            return N
        divides = N/2
        remain = N%2
        # print divides, remain
        return str(helper(divides))+str(remain)

    bin_string = str(helper(divides))+str(remain)
    # print bin_string
    bin_string = str(int(bin_string))
    # print bin_string

    # print bin_string

    # bin_string = ""
    bin_gap = 0
    max_gap = 0
    for c in bin_string:
        if c == "0":
            bin_gap += 1
        if c == "1":
            if bin_gap > max_gap:
                max_gap = bin_gap
            bin_gap = 0
        # print bin_gap, max_gap
    #return largest of bin_gap or max_gap (bin_gap can be greater if it is at very end)
    return max_gap
