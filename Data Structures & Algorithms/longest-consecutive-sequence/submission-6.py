class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_streak = 1
        curr_streak = 1
        last = None
        clean = (sorted(set(nums)))
        for num in clean:
            if num - 1 == last:
                curr_streak += 1
            else: 
                curr_streak = 1
            last = num
            longest_streak = max(curr_streak,longest_streak)
            
        return max(longest_streak,curr_streak)