from typing import List

class Solution:
    def solve(self, i: int, buy: int, prices: List[int], dp: List[List[int]]) -> int:
        if i >= len(prices):  # Base case: no more days left
            return 0
        
        if dp[i][buy] != -1:  # Return already computed value
            return dp[i][buy]
        
        if buy:
            # Two choices: Buy or Skip
            profit = max(
                -prices[i] + self.solve(i + 1, 0, prices, dp),  # Buy the stock
                self.solve(i + 1, 1, prices, dp)  # Skip buying
            )
        else:
            # Two choices: Sell or Skip
            profit = max(
                prices[i] + self.solve(i + 2, 1, prices, dp),  # Sell and cooldown
                self.solve(i + 1, 0, prices, dp)  # Skip selling
            )
        
        dp[i][buy] = profit
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Initialize a 2D dp array with -1
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.solve(0, 1, prices, dp)
