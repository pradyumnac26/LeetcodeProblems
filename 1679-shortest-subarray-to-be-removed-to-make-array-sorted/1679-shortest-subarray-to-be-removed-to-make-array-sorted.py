class Solution:
    def findLengthOfShortestSubarray(self, arr):
        N = len(arr)
        # Initialize pointers
        l, r = 0, N - 1

        # Remove prefix: Find largest sorted suffix
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        res = r  # Initial result: remove all elements to make suffix sorted

        # Remove postfix: Find largest sorted prefix
        while l + 1 < N and arr[l] <= arr[l + 1]:
            l += 1
        res = min(res, N - 1 - l)

        # Remove middle: Combine prefix and suffix while removing middle
        l, r = 0, N - 1
        while l < r:
            # Shrink valid window
            while r < N and l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
                r -= 1
            # Expand invalid window
            while r < N and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)  # Update the result
            if l + 1 < N and arr[l] > arr[l + 1]:  # Break if prefix is invalid
                break
            l += 1

        return res
