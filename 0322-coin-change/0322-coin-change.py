class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount + 1) 
        dp[0] = 0 

        if amount < 1 : 
            return 0
        
        for i in range(1, amount+1) : 
            for coin in coins : 
                if i >= coin : 
                    remainder = i - coin 
                    dp[i] = min(1+dp[remainder], dp[i])
        
        if dp[amount] != float('inf') : 
            return dp[amount]
        else : 
            return -1





        




        
        

        