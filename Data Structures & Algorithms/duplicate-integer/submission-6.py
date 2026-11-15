class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = len(set(nums))
        if setnums < len(nums):
            return True
        else: 
            return False
