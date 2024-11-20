class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Total counts of 'a', 'b', 'c'
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Check if it's possible to take k of each character
        if min(count) < k:
            return -1

        # Sliding Window to find the smallest window to remove
        res = float('inf')  # Initialize result as infinity
        l = 0
        n = len(s)

        for r in range(n):
            count[ord(s[r]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            
            # Update the result with the size of the current valid window
            res = min(res, n - (r - l + 1))

        return res
