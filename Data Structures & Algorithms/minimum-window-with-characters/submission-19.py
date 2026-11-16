class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        l = 0
        tCount = Counter(t)
        sCount = Counter()
        res = [-1,-1]
        minSoFar = float('infinity')
        requirements = 0 
        for r in range(len(s)):
            if s[r] in tCount:
                sCount[s[r]] += 1
                if sCount[s[r]] == tCount[s[r]]:
                    requirements += 1
            while requirements == len(tCount):
                if (r-l+1) < minSoFar:
                    res = [l,r]
                    minSoFar = r-l+1
                if s[l] in tCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        requirements -= 1 
                l += 1
        l,r = res 
        return s[l:r+1] if minSoFar != float('infinity') else ""