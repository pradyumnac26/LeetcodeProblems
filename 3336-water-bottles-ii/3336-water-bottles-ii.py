class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        full = numBottles
        empty = 0
        exchange = numExchange
        
        while full > 0:
            # drink all full bottles
            drank += full
            empty += full
            full = 0
            
            # try to exchange
            if empty >= exchange:
                empty -= exchange
                full += 1
                exchange += 1
            else:
                break
        
        return drank
