class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+*-/":
                if token == "+":
                    curr_ans = stack.pop() + stack.pop() 
                    stack.append(curr_ans)
                if token == '*':
                    curr_ans = stack.pop() * stack.pop()
                    stack.append(curr_ans)
                if token == "-":
                    second_operand = stack.pop()
                    first_operand = stack.pop()
                    curr_ans = first_operand - second_operand 
                    stack.append(curr_ans)
                if token == "/":
                    denominator = stack.pop()
                    numerator = stack.pop()
                    curr_ans = numerator / denominator 
                    stack.append(int(curr_ans))
            else:
                stack.append(int(token))
        ans = stack.pop()
        return int(ans)