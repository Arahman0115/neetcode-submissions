class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_ar = 0

        l,r = 0, len(heights) - 1
        while l <= r: 
            width = r - l
            area = min(heights[l],heights[r]) * width
            max_ar = max(max_ar,area)
            if max(heights) * width <= max_ar:
                return max_ar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max-ar 