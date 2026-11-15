class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"{":"}","(":")","[":']'}
        
        for par in s:
            if par in "([{":
                stack.append(par)
            elif not stack or par != pairs[stack.pop()]:
                return False
        return len(stack) == 0 
