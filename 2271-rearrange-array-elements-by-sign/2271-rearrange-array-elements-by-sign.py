class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posInd, negInd = 0,1
        ans = [0]*len(nums)

        for i in range(len(nums)) : 
            if nums[i] > 0 : 
                ans[posInd] = nums[i]
                posInd +=2 
            else : 
                ans[negInd] = nums[i] 
                negInd+=2
        return ans
        