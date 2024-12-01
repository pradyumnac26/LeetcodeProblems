class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, index, current_subset, unique_subsets):
            # Base case: If we have processed all elements
            if index == len(nums):
                # Sort the current subset and add it as a tuple to the set
                unique_subsets.add(tuple(sorted(current_subset)))
                return
            
            # Include the current element
            current_subset.append(nums[index])
            solve(nums, index + 1, current_subset, unique_subsets)
            current_subset.pop()  # Backtrack
            
            # Exclude the current element
            solve(nums, index + 1, current_subset, unique_subsets)
        
        unique_subsets = set()  # Set to store unique subsets
        solve(nums, 0, [], unique_subsets)
        
        # Convert the set of tuples back to a list of lists
        return [list(subset) for subset in unique_subsets]
