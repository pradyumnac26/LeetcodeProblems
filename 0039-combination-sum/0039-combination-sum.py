from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def find_combinations(i, arr, target, ds, ans):
            # Base case: If we've considered all elements
            if i == len(arr):
                if target == 0:
                    ans.append(list(ds))  # Add a copy of the current combination
                return
            
            # If the current element can be included (<= target)
            if arr[i] <= target:
                # Include the current element
                ds.append(arr[i])
                # Recur with the same index (allow repeated elements) and reduced target
                find_combinations(i, arr, target - arr[i], ds, ans)
                # Backtrack: Remove the last added element
                ds.pop()
            
            # Exclude the current element and move to the next index
            find_combinations(i + 1, arr, target, ds, ans)

        ans = []
        ds = []
        find_combinations(0, candidates, target, ds, ans)
        return list(ans)

