class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        l = 0 
        ans = 0
        while l < len(fruits) : 
            for r in range(len(baskets)) : 
                if fruits[l] <= baskets[r] : 
                    ans = ans + 1
                    baskets.remove(baskets[r])
                    break
            l = l+1
        return len(fruits) - ans

        