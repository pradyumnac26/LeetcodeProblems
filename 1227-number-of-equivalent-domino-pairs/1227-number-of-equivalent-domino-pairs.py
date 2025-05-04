from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Normalize domino as an ordered tuple
            result += count[key]         # Count how many have occurred so far
            count[key] += 1              # Update frequency

        return result
