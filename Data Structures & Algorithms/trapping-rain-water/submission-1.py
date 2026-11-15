class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        i,j = 0 , len(height) - 1
        left_max, right_max = height[0], height[-1]
        while i < j: 
            if left_max <= right_max:
                water += left_max - height[i]
                i+= 1
                left_max = max(height[i],left_max)
            else:
                water += right_max - height[j]
                j-=1 
                right_max = max(height[j], right_max)
        return water