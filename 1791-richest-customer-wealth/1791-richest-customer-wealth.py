class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = sum(accounts[0])
        for i in accounts : 
            maxi = max(maxi, sum(i))
        return maxi
        