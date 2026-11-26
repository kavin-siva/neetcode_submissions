from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]  # Bought on day 0
        sold = 0  # Impossible on day 0, safe baseline
        rest = 0  # Did nothing on day 0

        for price in prices[1:]:
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)

        