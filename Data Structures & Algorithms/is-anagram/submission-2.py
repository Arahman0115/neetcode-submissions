class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        ts = sorted(t)
        print(ts)
        print(ss)
        return ss == ts