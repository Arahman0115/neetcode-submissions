class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_ar = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = heights[top] * width
                max_ar = max(max_ar,area)
            stack.append(i)
        return max_ar