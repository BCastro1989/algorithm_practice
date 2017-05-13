class WordDistanceFinder:
    """
    This class will be given a list of words (such as might be tokenized
    from a paragraph of text), and will provide a method that takes two
    words and returns the shortest distance (in words) between those two
    words in the provided text.

    ::
      finder = new WordDistanceFinder(["the", "quick", "brown", "fox", "quick"])
      assert finder.distance("fox", "the") == 3
      assert finder.distance("quick", "fox") == 1

    "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
        (3 - 1) = 2 and (4 - 3) = 1.

    Since we have to return the shortest distance between the two words we return 1.

    """
    def __init__(self, words):
        # Implementation here
        self.words = words
        self.wordmap = {}

        for i, w in enumerate(words):
            if w not in self.wordmap:
                self.wordmap[w] = [i]
            else:
                self.wordmap[w].append(i)

    def distance(self, wordOne, wordTwo):
        # Implementation here
        #for words
        #note indexes of each word
        #note if appear more than once, where?

        w1_ind = self.wordmap[wordOne]
        w2_ind = self.wordmap[wordTwo]

        if wordOne == wordTwo:
            return 0

        min_diff = 99999999999

        #For testing, get idea of how many for loop runs
        runs = 0

        #find starting index
        min_w2 = w2_ind[0]
        w1_start_ind = 0
        for i, w1 in enumerate(w1_ind):
            runs += 1
            if w1 < min_w2:
                w1_start_ind = i
        for i, w2 in enumerate(w2_ind):
            runs += 1
            if w1 > min_w2:
                w2_start_ind = i

        for i in xrange(w1_start_ind,len(w1_ind)):
            w1 = w1_ind[i]
            #if index in w2 is larger than

            for j in xrange(w2_start_ind,len(w2_ind)):
                w2 = w2_ind[j]
                runs += 1
                diff = abs(w1 - w2)
                print w1, "v", w2, "=", diff
                if diff == 1:
                    return 1
                elif diff < min_diff:
                    min_diff = diff
                elif diff > min_diff:
                    break

        # print runs made vs. if every iteration of ever loop ran
        print runs, "/", str(len(w1_ind)*len(w2_ind)+len(w1_ind)+len(w2_ind))

        return min_diff


wdf = WordDistanceFinder(["fair", "fair", "fair", "fair", "fair", "scarborough", "fair", "parsley", "sage", "rosemary", "thyme", "ten", "eleven", "sage", "sage"])
ans = wdf.distance("sage","fair")
print ans
