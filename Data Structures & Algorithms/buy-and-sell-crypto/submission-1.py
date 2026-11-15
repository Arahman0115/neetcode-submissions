class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        n = len(prices)
        max_profit = 0
        for i in range(n):
            if prices[i] <= min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price    
                max_profit = max(max_profit, profit)
        return max_profit



