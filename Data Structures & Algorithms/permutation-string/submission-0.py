class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        freq = Counter()
        l = 0
        for r in range(len(s2)):
            freq[s2[r]] += 1
            while sum(freq.values()) > len(s1):
                freq[s2[l]] -= 1
                l += 1
            if freq == s1Count:
                return True
            
        return False
                
