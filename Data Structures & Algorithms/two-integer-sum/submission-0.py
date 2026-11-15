class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for key, value in enumerate(nums):
            diff = target - value
            if diff in dicto:
                return [dicto[diff],key]
            else:
                dicto[value] = key