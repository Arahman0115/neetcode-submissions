class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_ar = max(heights) * len(heights)
        curr_highest_ar = 0
        while i < j:
            distance = j - i
            area = distance * min(heights[i],heights[j])
            if max_ar <= area:
                return area
            curr_highest_ar = max(curr_highest_ar,area)
            if heights[i] < heights[j]:
                i+= 1
            else:
                j-=1 
        return curr_highest_ar