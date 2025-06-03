class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # say is sort it , so [1, 5], [3, 6], [4, 7] -> 1,6   4,7
        # line sweep, say arrived at 1, 3, 4, so cnt = 3 and then 
        # 
        nums.sort()
        merged = []
        start = nums[0][0]
        end = nums[0][1]
        merged.append([start, end])
        for i in range(1, len(nums)): 
            if merged and merged[-1][1] >= nums[i][0]: 
                merged[-1][1] = max(merged[-1][1], nums[i][1]) 
                print(merged)            
            else :
                merged.append([nums[i][0], nums[i][1]])
        
        cnt = 0 
        for x,y in merged : 
            cnt = cnt + y-x+1
        return cnt
