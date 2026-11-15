class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in dicto:
                return [dicto[diff], index]
            else:
                dicto[number] = index