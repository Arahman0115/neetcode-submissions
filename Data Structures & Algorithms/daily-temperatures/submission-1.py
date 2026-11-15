class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                temp, tempidx = stack.pop()
                res[tempidx] = i - tempidx 
            stack.append([value,i])
        return res

