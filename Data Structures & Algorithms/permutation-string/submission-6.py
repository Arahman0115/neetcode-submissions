class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        s1Count = Counter(s1)
        s2Count = Counter()

        for r in range(len(s2)):
            s2Count[s2[r]] += 1
            while sum(s2Count.values()) > sum(s1Count.values()):
                s2Count[s2[l]] -= 1
                l += 1
            if s1Count == s2Count:
                return True
        return False
            