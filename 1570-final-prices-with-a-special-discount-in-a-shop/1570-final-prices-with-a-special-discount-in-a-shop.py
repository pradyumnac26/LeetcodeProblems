class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        result = prices[:]  # Copy prices as the base result
        stack = []  # Monotonic stack to store prices

        # Traverse from the end of the array
        for i in range(n - 1, -1, -1):
            # Maintain a decreasing stack
            while stack and stack[-1] > prices[i]:
                stack.pop()
            # If stack is not empty, apply the discount
            if stack:
                result[i] -= stack[-1]
            # Push the current price onto the stack
            stack.append(prices[i])

        return result

 # Output: [9, 0, 1, 6]
