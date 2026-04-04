class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_low_price = prices[0]
        max_profit = 0

        for i, curr_price in enumerate(prices[1:]):
            curr_profit = curr_price - curr_low_price
            if(curr_profit > max_profit):
                max_profit = curr_profit
            if(curr_low_price > curr_price):
                curr_low_price = curr_price
        return max_profit
