class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = float('inf')
        maxi = float('-inf')
        for i in range(len(nums)): 
            if nums[i] < mini : 
                mini = nums[i] 
            if nums[i] > maxi :
                maxi = nums[i]
        print(mini) 
        print(maxi) 
        s = set(nums)
        res = [] 
        for i in range(mini, maxi+1): 
            if i not in s : 
                res.append(i)
        return res


        