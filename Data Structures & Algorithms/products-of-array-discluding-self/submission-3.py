class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        n = len(nums)
        l = 1 
        for i in range(n):
            res[i] *= l
            l *= nums[i]
        r = 1
        for i in range(n-1,-1,-1):
            res[i] *= r
            r *= nums[i]
        return res