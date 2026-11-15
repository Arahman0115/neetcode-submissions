class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = max(heights)
        maxAr = 0 

        l,r = 0,len(heights) - 1
        while l < r: 
            width = (r-l)
            arr = width * min(heights[l],heights[r])
            maxPossible = maxH * len(heights) 
            if arr >= maxPossible:
                return arr
            maxAr = max(maxAr, arr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxAr

            
                
