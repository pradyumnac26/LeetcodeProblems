class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        # take 4 put in stack and then go to 2 see that its 2 < 4 have to do stack.pop 
        cnt = 0 
        stack = [] 
        stack.append(nums[0])
        for i in range(1, len(nums)): 

            if nums[i] >= stack[-1] : 
                stack.append(nums[i])
        return len(stack)



            





