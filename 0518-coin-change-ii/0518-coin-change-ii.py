class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # we sawe miimum num ber, now we have to find number of ways... 
        dp = [0]*(amount+1) 
        dp[0] = 1
        for c in coins : 
            for a in range(1, amount+1) : 
                if a >= c : 

                    dp[a]+= dp[a-c]
        return dp[amount]
        