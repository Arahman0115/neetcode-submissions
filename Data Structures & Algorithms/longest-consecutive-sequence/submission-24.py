class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        longest = 1
        Last = None
        currStreak = 1 
        sortedNums = sorted(set(nums)) 
        for num in sortedNums: 
            if num - 1 == Last:
                currStreak += 1
                longest = max(longest,currStreak)
            else:
                currStreak = 1
            Last = num
        return max(longest,currStreak)

