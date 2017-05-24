#
# To handle capitalized words, there were lots of heuristics
#  and approaches we could have used, each with their own strengths
#  and weaknesses. Open-ended questions like this can really separate
#  good engineers from great engineers.

# Good engineers will come up with a solution,
# but great engineers will come up with several solutions,
#  weigh them carefully, and choose the best solution for 
#  the given context. So as you're running practice questions,
#   challenge yourself to keep thinking even after you have a
#   first solution. See how many solutions you can come up with.
#   This will grow your ability to quickly see multiple ways to
#    solve a problem, so you can figure out the best solution.
#    And use the hints and gotchas on each Interview Cake
#    question—they're designed to help you cultivate this skill.


def wordcloud(arg):

    def add_to_dict(word):
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    def is_upper(c):
        if c == c.upper():
            return True
        return False

    def is_name(word):
        if word[0] == word[0].upper() and word[:-2] == "'s'":
            return True
        return False

    word_freq = {}
    word = ""
    new_sentance = True
    proper_noun = False
    for c in arg:
        if c.isalpha():
            print c, "cap:", is_upper(c), "nsentance:", new_sentance
            if new_sentance and is_upper(c):
                new_sentance = False
            elif not new_sentance and is_upper(c):
                proper_noun = True
            word += c
        elif c in " -,":
            print word, "1pnoun:", proper_noun
            if not proper_noun:
                word = word.lower()
            print word, "2pnoun:",proper_noun
            proper_noun = False
            if word:
                add_to_dict(word)
            word = ""
        elif c in ".?!":
            new_sentance = True
        else:
            print c, "!!!!"
            # add_to_dict(word)

    return word_freq
#'After beating the eggs, Dana read the next step: add milk-and-eggs, then add flour and sugar. We came, we saw, we conquered... then we ate Bill\'s (Mille-Feuille) cake. The bill came to five dollars.
print wordcloud('The bill was paid by Bill, great guy!')





# def my_function(arg):
#     # write the body of your function here
#     words = arg.split(" ")
#     word_freq = {}
#
#     def add_to_dict(word):
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1
#
#     def is_name(word):
#         if word[0] == word[0].upper() and word[:-2] == "'s'":
#             return True
#         return False
#
#     for word in words:
#         word = word.strip(":,.:'\"|\}{~`!@#$%^&*()_-+=")
#         if not is_name(word):
#             word = word.lower()
#         hypenated_w = word.split("-")
#         if len(hypenated_w) == 1:
#             add_to_dict(word)
#         else:
#             for word in hypenated_w:
#                 add_to_dict(word)
#
#     return word_freq


# run your function through some test cases here
# remember: debugging is half the battle!
