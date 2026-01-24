class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # minimized maximum sum pair , meaning 
        # firstly there can be multiple pairs, so say we choose a set of pairs find the sum of each pair and then take max of the pair then we get the max pair sum, and then we will store it somewhee, and then lets try anoter combination of pairs, and take max and push to the res, finally we wil take the min of the res and return. this i the idea, can go with brute force first
        # one thing to observe is that , we wold get the max sum when a max number is involved right, and then when we take the minimum, we are choosing thenumbers with minimums uk what i mean riht 
        # so what datastrucure o use or what logic or pattern comes to my mind 
        res = [] 
        l = 0 
        r = len(nums)-1
        nums.sort()
        while l <r : 
            sumi = nums[l] + nums [r] 
            res.append(sumi) 
            l+=1 
            r-=1 
        return max(res)



        