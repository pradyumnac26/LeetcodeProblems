from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        hmap = Counter(nums)
        for freq in hmap.values():
            if is_prime(freq):
                return True 
        return False

        