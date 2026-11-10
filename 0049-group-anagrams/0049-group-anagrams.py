from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)  #each uninitialized key gets an empty list as its value
        for s in strs:
            count = [0] * 26 #initializing our frequency array to have 26 zeros in it
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)  
            #after all neccessary key are updated, it is made into a
        return list(result.values())