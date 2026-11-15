class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        last = None
        longest_streak = 1
        count = 1
        cleaned = (sorted(set(nums)))
        for n in cleaned:
            if n - 1 == last:
                count += 1
            else:
                count = 1
            longest_streak = max(longest_streak, count)
            last = n
        return max(longest_streak,count)


