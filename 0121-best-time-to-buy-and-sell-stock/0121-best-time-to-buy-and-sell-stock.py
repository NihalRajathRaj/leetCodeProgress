class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(buy, -price)
            sell = max(sell, buy + price)
        return sell
            