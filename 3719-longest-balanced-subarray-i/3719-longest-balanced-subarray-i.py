class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # number of distinct even numbers == number of distinct odd numbers in a subarray, and return the longest subarray.. 
        # store the distinctness in a hmap, and then cnt of the numbers in 
        # i am at 2 , even = 1, and 5, odd = 1, and 4, even = 2, and 3, odd = 2, so there is a distinct of 
        # 1, odd=1, 2, even =1, 3, odd= 2 , 2 sits the same so even =1 

        maxi = 0 

        for i in range(len(nums)) : 
            even = set()
            odd = set() 
            for j in range(i, len(nums)): 
                if nums[j]%2 == 0 : 
                    even.add(nums[j])
                if nums[j] %2 !=0 : 
                    odd.add(nums[j]) 
                if len(even) == len(odd) : 
                    maxi = max(j-i+1, maxi)
        return maxi




        
        
