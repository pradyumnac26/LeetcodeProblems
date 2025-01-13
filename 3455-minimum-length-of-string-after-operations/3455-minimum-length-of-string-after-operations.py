from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        # Step 1: Count character frequencies
        freq = Counter(s)

        # Step 2: Calculate the minimum length
        length = 0
        for count in freq.values():
            if count % 2 == 1:  # If the frequency is odd
                length += 1  # One unmatched character remains
            else:  # If the frequency is even
                length += min(2, count)  # At most two characters can remain

        return length
