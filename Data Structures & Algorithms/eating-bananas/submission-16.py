class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        min_k = max(piles)
        while l < r:
            t = h
            k = (l+r) // 2
            for p in piles:
                t -= math.ceil(p/k)
            if t >= 0:
                min_k = min(min_k,k)
                r = k
            else:
                l = k + 1
        return min_k 

