class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0 
        res = [-1,-1]
        if t == "": return ""
        if len(t) > len(s):
            return ""
        tCounter = Counter(t)
        sCounter = Counter()
        minSoFar = float('infinity')
        requirements = 0
        for r in range(len(s)):
            if s[r] in tCounter:
                sCounter[s[r]] += 1
                if sCounter[s[r]] == tCounter[s[r]]:
                    requirements += 1
            while len(sCounter) == len(tCounter) and requirements == len(tCounter): 
                if ((r-l) + 1) <= minSoFar: 
                    res = [l,r]
                    minSoFar = (r-l) + 1
                if s[l] in tCounter:
                    sCounter[s[l]] -= 1
                    if sCounter[s[l]] < tCounter[s[l]]:
                        requirements -= 1
                l += 1
        l,r = res
        return s[l:r+1] if minSoFar != float('infinity') else ""