class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numset = sorted(set(nums))
        last = None 
        curr_length = 1
        max_len = 0 
        for number in numset:
            if number - 1 == last:
                curr_length += 1
            else:
                max_len = max(curr_length, max_len)
                curr_length = 1 
            last = number
        return max(curr_length,max_len)