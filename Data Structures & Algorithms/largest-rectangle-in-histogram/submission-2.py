class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_ar = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_ar = max(max_ar, height * (i - index))
                start = index           
            stack.append([start,h])
        for i,h in stack:
            max_ar = max(max_ar, h * (len(heights) - i))
        return max_ar