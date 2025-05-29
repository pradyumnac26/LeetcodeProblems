class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [] 
        #first occurrence 
        l , r = 0, len(nums)-1
        ans = -1
        while l <=r :
            mid = (l + r) // 2
            if nums[mid] == target: 
                ans = mid
                r = mid - 1
            elif nums[mid] < target : 
                l = mid + 1 
            else : 
                r = mid -1 
        res.append(ans)
        l, r = 0 , len(nums) - 1
        ans2 = -1
        while l <= r : 
            mid = (l+r)//2
            if nums[mid] == target: 
                ans2 = mid 
                l = mid + 1
            elif nums[mid] < target : 
                l = mid + 1 
            else : 
                r = mid - 1
        res.append(ans2)
        return res if len(res) > 0 else [-1, -1]


        
        


                



