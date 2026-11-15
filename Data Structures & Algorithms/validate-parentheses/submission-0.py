class Solution:
    def isValid(self, s: str) -> bool:
        dicto = {"(":")","{":"}","[":"]"}
        stack = []
        for brack in s:
            if brack in '[{(':
                stack.append(brack)
            elif not stack or brack != dicto[stack.pop()]:
                return False
        return len(stack) == 0