class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = defaultdict(list)
        for word in strs:
            sortedword = ''.join(sorted(word))
            dicto[sortedword].append(word)
        
        return list(dicto.values())