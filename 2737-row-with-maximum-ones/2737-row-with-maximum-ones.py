from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # Helper function to find the lower bound of 1 in a sorted row
        def lowerbound(arr, m, x):
            low, high = 0, m - 1
            ans = m  # Default to the end of the row if no 1 is found
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        cnt_max = 0
        index = 0
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns
        for i in range(n):
            # Pass the i-th row and its length to lowerbound
            mat[i].sort()
            cnt_ones = m - lowerbound(mat[i], m, 1)  # Number of 1s in the row
            if cnt_ones > cnt_max :
                cnt_max = cnt_ones
                index = i
        return [index, cnt_max]
