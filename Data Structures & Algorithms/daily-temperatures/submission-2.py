class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index in range(len(temperatures)):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = index - prev_index
            stack.append(index)
        return res