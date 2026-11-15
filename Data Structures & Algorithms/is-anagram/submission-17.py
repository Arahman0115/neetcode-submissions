class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tdicto = defaultdict(int)
        sdicto = defaultdict(int)
        for i in range(len(s)):
            tdicto[t[i]] += 1
            sdicto[s[i]] += 1
        for char in s: 
            if tdicto[char] != sdicto[char]:
                return False
        return True
        