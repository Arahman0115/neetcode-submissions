class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0 
        n = len(prices)
        for i in range(n - 1):
            j = len(prices) - 1
            while i < j: 
                profit = prices[j] - prices[i]
                max_profit = max(profit,max_profit)
                j -= 1
        return max_profit

