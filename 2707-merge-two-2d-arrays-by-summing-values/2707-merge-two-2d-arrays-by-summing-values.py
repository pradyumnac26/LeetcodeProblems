class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        x = {} 
        for nums in nums1 : 
            x[nums[0]] = nums[1] 

        for nums in nums2 : 
            x[nums[0]] = x.get(nums[0], 0) + nums[1] 

        b = [] 
        for i, j in sorted(x.items()) : 
            b.append([i,j])
        return b

