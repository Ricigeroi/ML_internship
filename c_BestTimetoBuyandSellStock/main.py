class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = max(prices)
        profit = 0

        for item in prices:
            if item < price:
                price = item
            else:
                profit = max(profit, item - price)

        return profit