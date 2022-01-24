class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float('inf') # to find a min value
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit
        