class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set() 
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in stringSet:
                stringSet.remove(s[l])
                l += 1
            stringSet.add(s[r])
            maxLen=max(maxLen, r-l+1)
        return maxLen