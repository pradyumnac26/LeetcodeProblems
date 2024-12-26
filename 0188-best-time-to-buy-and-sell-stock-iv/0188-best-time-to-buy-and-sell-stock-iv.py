from typing import List

class Solution:
    def solve(self, i: int, buy: int, k: int, prices: List[int], dp: List[List[List[int]]]) -> int:
        if i == len(prices) or k == 0:
            return 0
        
        if dp[i][buy][k] != -1:
            return dp[i][buy][k]
        
        if buy:
            profit = max(
                -prices[i] + self.solve(i + 1, 0, k, prices, dp),  # Buy the stock
                self.solve(i + 1, 1, k, prices, dp)  # Skip buying
            )
        else:
            profit = max(
                prices[i] + self.solve(i + 1, 1, k - 1, prices, dp),  # Sell the stock
                self.solve(i + 1, 0, k, prices, dp)  # Skip selling
            )
        
        dp[i][buy][k] = profit
        return profit

    def maxProfit(self,k:int, prices: List[int]) -> int:
        n = len(prices)
        # Initialize a 3D dp array with -1
        dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        return self.solve(0, 1, k, prices, dp)
