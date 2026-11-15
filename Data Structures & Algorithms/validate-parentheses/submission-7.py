class Solution:
    def isValid(self, s: str) -> bool:
        pars = {
            "(":")",
            "[":']',
            '{':'}'
        }
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif not stack or char != pars[stack.pop()]:
                return False
        return len(stack) == 0 