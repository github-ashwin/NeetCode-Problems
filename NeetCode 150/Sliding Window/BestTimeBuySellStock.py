from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] # initially, first value as min_price
        max_profit = 0

        # iterate through all values to find the min_price and max_profit
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        
        return max_profit