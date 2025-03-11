from collections import Counter
class Solution:


    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            count = 0
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1  # Use this character
                    count += 1 + backtrack(counter)  # Count this sequence and recurse
                    counter[char] += 1  # Backtrack (restore character count)
            return count

        return backtrack(Counter(tiles))

        