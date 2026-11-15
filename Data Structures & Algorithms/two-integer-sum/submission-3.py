class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for i, num in enumerate(nums): 
            diff = target - num
            if diff in dicto: 
                return [dicto[diff], i] 
            else:
                dicto[num] = i 