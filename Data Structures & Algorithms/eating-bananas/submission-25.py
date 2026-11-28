class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        minRate = max(piles)

        while l <= r:
            t = h
            k = (l+r) // 2
            for p in piles:
                t -= math.ceil(p/k)
            if t >= 0:
                minRate = min(minRate,k)
                r = k - 1
            else:
                l = k + 1
        return minRate 
