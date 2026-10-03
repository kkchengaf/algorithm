#O(m^2) naive build tree, suitable for short word, O(m^2n) 
#Ukkonen's algorithm: build tree in O(n) time for alphabet, O(nlogn) in general


#for each starting index of word, insert into trie, each prefix of the suffix is visited while traversing

# application 1: searching for string t as a substring of some words
# application 2: count number of occurence of string t in some words, "_" count number of occurence of the string
# not very efficient application:
# application 3: longest repeated substring in s
# application 4: longest common substring
# application 5: longest palindrome substring 


        for word in words:
            for i in range(len(word)):
                t = trie
                for c in word[i:]:
                    if c not in t:
                        t[c] = {"_":0}
                    t = t[c]
                    t["_"] += 1


        for word in words:
            t = trie
            for c in word:
                t = t[c]

