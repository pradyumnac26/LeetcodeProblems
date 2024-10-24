class Solution:
    def grayCode(self, n: int) -> List[int]:
            result = []
            for i in range(1 << n):  # Loop over the range [0, 2^n)
                result.append(i ^ (i >> 1))  # Apply the formula for Gray code
            return result


        