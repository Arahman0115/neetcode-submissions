class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        freq = Counter()
        longest = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            while ( (r-l) + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            longest=max(longest,r-l+1)
        return longest 