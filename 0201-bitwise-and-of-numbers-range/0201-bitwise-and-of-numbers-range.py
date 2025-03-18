class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0  # Count how many bits we shift
        while left < right:
            left >>= 1  # Shift right to remove differing bits
            right >>= 1
            shift += 1

        return left << shift