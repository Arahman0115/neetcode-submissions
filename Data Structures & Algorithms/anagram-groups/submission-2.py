from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for word in strs:
            sw = ''.join(sorted(word))
            dicto[sw].append(word)
        return dicto.values()