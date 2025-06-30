class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # lingest harmonious subsequence-> diff between max and min value is exactly 1 in subsequence. 
        x = Counter(nums)
        z = dict(sorted(x.items()))
        print(z)
        maxi = 0

        for i in z.keys(): 
            if i+1 in z : 
                maxi = max(maxi, z[i] + z[i+1])
        return maxi



        
        


        