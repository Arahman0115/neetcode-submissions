class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0,len(height) - 1
        left_max,right_max = height[0],height[-1]
        while l <= r:
            if left_max < right_max:
                water += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            
            else:
                water += right_max - height[r]
                r -=1 
                right_max = max(right_max, height[r])
        return water