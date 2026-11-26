class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        minNum = float('infinity')
        while l <= r:
            m = (l+r) // 2
            minNum = min(minNum,nums[m]) 
            if nums[m] > nums[r]:
                # left sort
                l = m + 1
            else:
                # right sort 
                r = m - 1
        return minNum
        
            