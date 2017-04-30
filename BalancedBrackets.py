"""
Date: 4/29/17
Source: HR + CTCI
Time: 10-15min
Fairly straightforward again, this was a "medium" difficulty problem. I took
the right general approach but I could have done it in a lot less lines. The
examples in the discussion boards use a dict to make the code cleaner/smaller

A example from discussion boards:

def is_matched(expression):
    pairs_dict = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in expression:
        if char in pairs_dict.values():
            stack.append(char)
        elif char in pairs_dict:
            if not stack or pairs_dict[char] != stack.pop():
                return False
    return not stack

"""

def is_matched(expression):
    braks = "|"
    #matched = True
    for c in expression:
        if c == "{":
            braks += "c"
        if c == "[":
            braks += "s"
        if c == "(":
            braks += "p"
        if c == "}":
            if braks[-1] == "c":
                braks = braks[:-1]
            else:
                return False
        if c == "]":
            if braks[-1] == "s":
                braks = braks[:-1]
            else:
                return False
        if c == ")":
            if braks[-1] == "p":
                braks = braks[:-1]
            else:
                return False
    if len(braks) != 1:
        return False
    return True

    return matched
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
