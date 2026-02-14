class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 1 glass -> 1 row [1]
        # 2 glasses -> 2 rows [1] and [0.5. 0.5]
        # 3 glasses -> 2 rows. [1] and [1 1]
        # 4 glasses -> 3 rows , [1], [1 1] , [0.25 0.5 0.25 ]
        # 5 glasses -> 3 rows -> [0.5 1 0.5]
        # 6 glasses -> 4 rows -> [0.75 1 0.75] [0 0.25 0.25 0]
        # 1 
        # 2 glasses means 
        # 
        dp = [[0]*100 for _ in range(100)]
        if poured == 0 : 
            return 0

        dp[0][0]= poured 
        for i in range(query_row): 
            for j in range(i+1) : 
                if dp[i][j] > 1 : 
                    excess = (dp[i][j]-1)/2
                    dp[i+1][j]+=excess
                    dp[i+1][j+1]+= excess
        return min(1, dp[query_row][query_glass])






        