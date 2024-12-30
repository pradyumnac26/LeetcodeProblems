class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007
        
        # Memoization dictionary to store computed results for subproblems
        memo = {}

        # Recursive function to calculate the number of ways to form a string of length `i`
        def f(i):
            # Base case: if i exceeds high, return 0 (invalid)
            if i > high:
                return 0
            
            # If the result for this subproblem is already computed, return it from memo
            if i in memo:
                return memo[i]
            
            # Recursive case: count ways to extend by '0' and '1'
            count = 0
            if i >= low:
                count += 1  # This is a valid good string of length i
            # Extend by '0' (i + zero) and '1' (i + one)
            count += f(i + zero)
            count += f(i + one)
            count %= MOD  # Apply modulo to prevent overflow

            # Store the result in memo before returning
            memo[i] = count
            return count
        
        # Start the recursion from length 0
        return f(0)