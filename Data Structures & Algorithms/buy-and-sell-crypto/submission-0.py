class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0

        sell = 1

        if len(prices) == 1:
            return 0

        max_val = 0

        while sell < len(prices):
            if prices[sell] - prices[buy] <= 0:
                buy = sell
            max_val = max(max_val, prices[sell] - prices[buy])

            sell += 1
        return max_val