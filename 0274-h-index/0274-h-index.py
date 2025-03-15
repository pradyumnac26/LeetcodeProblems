from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort citations in descending order
        h = 0  # Initialize h-index
        for i, c in enumerate(citations):
            if c >= i + 1:  # If the citation count is at least (i+1)
                h = i + 1
            else:
                break  # Stop when condition fails
        return h

