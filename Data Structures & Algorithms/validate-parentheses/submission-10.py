class Solution:
    def isValid(self, s: str) -> bool:
        maps = {
            ')':'(','}':'{',']':'['
        }
        stack = []
       
        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack or stack.pop() != maps[char]:
                return False
        return len(stack) == 0

        