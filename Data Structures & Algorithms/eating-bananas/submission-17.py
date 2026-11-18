class Solution:
    def minEatingSpeed(self, piles, h):
        l,r = 1,max(piles)
        minRate = float('infinity')

        while l <= r: 
            k = (l+r) // 2
            t = h
            for p in piles:
                t -= math.ceil(p/k)
            if t >= 0:
                minRate = min(minRate,k)
                r = k - 1
            if t < 0: 
                l = k + 1
        return minRate
