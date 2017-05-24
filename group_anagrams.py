
#Given Arr of strings, group together anagrams
#For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
grams = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "act"]

from collections import Counter

def group_anagrams(words):

    #w_freq = Counter(words)
    #for every word in list
        #look at freq of letters
    freqs = []

    #total : O*N*m
    for w in words:#O(N)
        l_freq = dict(Counter(w))#O(m)
        # print dict(l_freq)
        freqs.append(l_freq)



    grouped = []
    for i, freq1 in enumerate(freqs):
        anagrams = []
        for j, freq2 in enumerate(freqs):
            # print anagrams
            # print (i, j, words[i], words[j])
            if freq1 == freq2 and i != j and freq1:#and not seen():
                anagrams.append(words[i])
                anagrams.append(words[j])
                freqs[i] = None
                freqs[j] = None
        if anagrams:
            grouped.append(anagrams)

    # print anagrams

    return grouped

    #compare to freq of letters of all words to one another


print (group_anagrams(grams))
