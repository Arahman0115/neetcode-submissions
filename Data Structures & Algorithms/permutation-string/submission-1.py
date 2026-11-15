class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = Counter()

        l = 0
        for r in range(len(s2)):
            s2Count[s2[r]] += 1
            while sum(s2Count.values()) > len(s1):
                s2Count[s2[l]] -= 1
                l += 1
            if s1Count == s2Count:
                return True
        return False
            