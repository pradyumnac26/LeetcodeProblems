class Solution:
    def mincostTickets(self, days, costs):
        # Create a set to track which days are travel days
        isTravelNeeded = set(days)
        
        # Memoization table to store the minimum cost for each day
        dp = [-1] * (days[-1] + 1)

        # Recursive function to calculate the minimum cost
        def solve(dp, days, costs, currDay):
            # Base case: If we've passed the last travel day, no more cost is needed
            if currDay > days[-1]:
                return 0
            
            # If it's not a travel day, skip to the next day
            if currDay not in isTravelNeeded:
                return solve(dp, days, costs, currDay + 1)
            
            # If the cost is already computed for this day, return it
            if dp[currDay] != -1:
                return dp[currDay]
            
            # Option 1: Buy a 1-day pass
            oneDay = costs[0] + solve(dp, days, costs, currDay + 1)
            
            # Option 2: Buy a 7-day pass
            sevenDay = costs[1] + solve(dp, days, costs, currDay + 7)
            
            # Option 3: Buy a 30-day pass
            month = costs[2] + solve(dp, days, costs, currDay + 30)
            
            # Store the minimum cost for the current day and return it
            dp[currDay] = min(oneDay, min(sevenDay, month))
            return dp[currDay]
        
        # Start the recursion from day 1
        return solve(dp, days, costs, 1)
