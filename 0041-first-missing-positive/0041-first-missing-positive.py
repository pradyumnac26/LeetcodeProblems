class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort() 
        smallest = 1 
        for n in nums : 
            if n == smallest : 
                smallest+=1
            elif n > smallest:
                break 
        return smallest
        