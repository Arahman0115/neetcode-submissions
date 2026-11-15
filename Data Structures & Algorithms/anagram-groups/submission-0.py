import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramdict = collections.defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagramdict[sorted_word].append(word)
        return anagramdict.values()
        