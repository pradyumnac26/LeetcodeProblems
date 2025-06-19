class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # nums and integer k, 
        # return minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequences is at most k 
        # sort firstly - [1, 2, 3, 5, 6]
        # now 1 , 2, , 3 cnt = 1 , cnt =2 
        nums.sort()
        mini = float('inf')
        maxi = float('-inf')
        cnt = 1
        for i in range(len(nums)): 
            mini = min(mini, nums[i])
            maxi = max(maxi, nums[i])
            if maxi - mini > k :
                cnt = cnt + 1  
                mini = maxi
        return cnt 



        