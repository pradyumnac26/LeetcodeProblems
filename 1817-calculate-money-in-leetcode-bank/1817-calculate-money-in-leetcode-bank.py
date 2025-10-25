class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1 
        amount = 0 
        total = 0 
        x = 8
        for i in range(1, n+1): 
            amount = amount + 1
            if i == x : 
                start = start + 1 
                amount = start 
                x =x+7

            total = total + amount
        return total



        
        