from collections import Counter

class Solution:
    def findEvenNumbers(self, digits):
        count = Counter(digits)
        result = set()

        # Try all 3-digit numbers from 100 to 999
        for num in range(100, 1000):
            a, b, c = num // 100, (num // 10) % 10, num % 10
            # Check even and digits exist
            if num % 2 == 0:
                candidate = Counter([a, b, c])
                # Check if we have enough of each digit
                if all(candidate[d] <= count[d] for d in candidate):
                    result.add(num)

        return sorted(result)

