from collections import Counter
class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        tCount = Counter(t)
        sCount = Counter()
        print(tCount.items())
        l = 0 
        results = []
        minSoFar = len(s)
        requirements = 0 
        bestWindow = None

        for r in range(len(s)):
            if s[r] in tCount:
                sCount[s[r]] += 1
                if sCount[s[r]] == tCount[s[r]]:
                    requirements += 1
                    
            while len(sCount) == len(tCount) and requirements == len(tCount): 
                currString = s[l:r+1]
                if ((r-l) + 1) <= minSoFar:
                    bestWindow = s[l:r+1]
                    minSoFar = (r-l) + 1
                
                if s[l] in tCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        requirements -= 1
                l += 1
        
        return bestWindow if bestWindow else ""

    # Checking for matches 