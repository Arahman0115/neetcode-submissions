class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in dicto:
                return [dicto[diff],i]
            else:
                dicto[val] = i 