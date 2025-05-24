from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Create a list of tuples: (value, distance from x)
        distance_list = [(num, abs(num - x)) for num in arr]
        
        # Sort by distance first, then by value
        sorted_list = sorted(distance_list, key=lambda item: (item[1], item[0]))

        # Take the first k elements and extract the numbers
        result = [item[0] for item in sorted_list[:k]]

        # Return result sorted by value (as per problem requirement)
        return sorted(result)






        