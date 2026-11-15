class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = index - idx
            stack.append([value,index])
        return res
