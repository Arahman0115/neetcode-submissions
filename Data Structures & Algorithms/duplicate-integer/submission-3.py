class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dicto = []
         for number in nums:
            if number in dicto:
                return True
            else:
                dicto.append(number)
                print(dicto)
         return False
