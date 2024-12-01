from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def bs(arr: List[int], target: int) -> int:
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1  # Return -1 if not found

        arr.sort()  # Sorting the array

        for i in range(len(arr)):
            target = 2 * arr[i]
            index = bs(arr, target)
            if index != i and index >= 0:  # Check valid index and not same element
                return True
        return False
