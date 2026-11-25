class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float('infinity')

        l,r = 0,len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            minNum = min(minNum,nums[m])
            if nums[m] > nums[r]:
                # we are in the left sort
                l = m + 1
            else:
                r = m - 1
        return minNum
