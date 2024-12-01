from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def find_combinations(index, arr, target, ds, ans):
            # Base case: If we've reached the end of the array
            if index == len(arr):
                if target == 0:
                    ans.append(list(ds))  # Add the current combination
                return
            
            # Pick the current element if it's not greater than the target
            if arr[index] <= target:
                ds.append(arr[index])
                # Move to the next index (element can only be picked once)
                find_combinations(index + 1, arr, target - arr[index], ds, ans)
                # Backtrack: Remove the last added element
                ds.pop()
            
            # Skip duplicates: Only consider the next element if it's different
            next_index = index + 1
            while next_index < len(arr) and arr[next_index] == arr[index]:
                next_index += 1
            
            # Skip the current element and move to the next unique index
            find_combinations(next_index, arr, target, ds, ans)

        # Sort the candidates to handle duplicates
        candidates.sort()
        ans = []
        ds = []
        find_combinations(0, candidates, target, ds, ans)
        return ans

# Test the function
solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

