class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(filter(str.isalnum, s)).lower()
        return filtered[::-1] == filtered
