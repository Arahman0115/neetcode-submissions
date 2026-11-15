class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            dicto[sorted_word].append(word)
        return list(dicto.values())

