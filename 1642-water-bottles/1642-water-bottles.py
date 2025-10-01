class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles 
        rem = 0
        toDrink = numBottles
        empty = numBottles
        while empty >= numExchange : 
            toDrink = empty // numExchange 
            cnt = cnt + toDrink 
            empty = empty % numExchange + toDrink
        return cnt





        