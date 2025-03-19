class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = [] 
        nums_ser = set(nums)
        for i in range(1, len(nums)+1) : 
            if i not in nums_ser : 
                x.append(i)
        return x


        