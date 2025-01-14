from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Initialize sets to track seen elements and common elements
        seen_A = set()
        seen_B = set()
        common = set()
        result = []

        # Iterate through both arrays simultaneously
        for a, b in zip(A, B):
            seen_A.add(a)
            seen_B.add(b)

            # Add to the common set if a number is seen in the opposite array
            if a in seen_B:
                common.add(a)
            if b in seen_A:
                common.add(b)

            # Add the size of the common set to the result
            result.append(len(common))

        return result
