from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sumi = 0

        for i in range(len(nums)):
            n = nums[i]
            cnt = 2
            res = [1, n]

            for j in range(2, math.isqrt(n) + 1):
                if n % j == 0:
                    other = n // j

                    if other == j:       
                        cnt += 1
                        res.append(j)
                    else:
                        cnt += 2
                        res.append(j)
                        res.append(other)

                    if cnt > 4:
                        break

            if cnt == 4:
                sumi += sum(res)

        return sumi
