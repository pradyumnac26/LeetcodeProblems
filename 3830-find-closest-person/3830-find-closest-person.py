class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) < abs(y-z) : 
            return 1 
        elif abs(y-z) < abs(x-z) : 
            return 2 
        else : 
            return 0

        