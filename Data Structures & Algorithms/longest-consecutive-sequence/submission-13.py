class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        Last = None
        longest_streak = 1
        curr_streak = 1
        cleaned = sorted(set(nums))
        for num in cleaned:
            if num - 1 == Last:
                curr_streak += 1
                longest_streak = max(longest_streak,curr_streak)
            else:
                curr_streak = 1
            Last = num
        return longest_streak
            