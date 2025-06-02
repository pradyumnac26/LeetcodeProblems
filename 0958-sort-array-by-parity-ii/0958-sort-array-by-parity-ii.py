class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # my case i is the odd index and j is the even index
        # say if i have [7, 2, 5, 4, 2, 1, 3, 2] -> [2, 7, 5, 4].
        # say i have [2, 1, 4, 3]
        # 
        i = 1
        j = 0
        while i < len(nums) and j < len(nums): 
            if nums[j]%2 == 0 : 
                j = j + 2
            elif nums[i]%2 == 1 : 
                i = i + 2
            else : 
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 2
                j = j +2
        return nums
            


        