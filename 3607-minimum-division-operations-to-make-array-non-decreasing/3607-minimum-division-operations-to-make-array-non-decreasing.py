from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0  # To count the number of operations

        # Traverse the array from right to left
        for i in range(n-1, 0, -1):
            # While the current element is greater than the next one
            while nums[i-1] > nums[i]:
                # Find the largest proper divisor of nums[i-1] that allows reduction
                ans = self.giveMe(nums[i-1])
                if ans == 1:  # If the divisor is 1, we can't reduce further, return -1
                    return -1
                nums[i-1] //= ans  # Reduce nums[i-1] by dividing it by ans
                op += 1  # Increment the operation count

        return op  # Return the total number of operations

    def giveMe(self, x: int) -> int:
        """
        Finds the largest proper divisor of x.
        If x is prime, the largest proper divisor is 1.
        """
        # Use the get_proper_divisors logic to find the largest divisor
        divisors = self.get_proper_divisors(x)
        return divisors[0] if divisors else 1  # Return the largest divisor or 1 if no divisor exists

    def get_proper_divisors(self, x: int) -> List[int]:
        """
        Returns all proper divisors of x in descending order.
        """
        divisors = []
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                if i < x:
                    divisors.append(i)
                if x // i != i and x // i < x:
                    divisors.append(x // i)
        divisors.sort(reverse=True)  # Sort divisors in descending order
        return divisors
