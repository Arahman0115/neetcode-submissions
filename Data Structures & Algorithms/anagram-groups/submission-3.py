class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for word in strs:
            cleaned_word = ''.join(sorted(word))
            if cleaned_word in dicto:
                dicto[cleaned_word].append(word)
            else:
                dicto[cleaned_word].append(word)
        return list(dicto.values())
