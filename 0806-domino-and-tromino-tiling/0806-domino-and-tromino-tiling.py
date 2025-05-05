class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        A = [0] * (n + 1)
        A[0], A[1], A[2], A[3] = 0, 1, 2, 5

        for i in range(4, n + 1):
            A[i] = (2 * A[i - 1] + A[i - 3]) % mod
        
        return A[n]