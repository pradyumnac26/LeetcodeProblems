class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # clarification qns : what if nums is empty ? return -1 as well ? 
        # so let me go through the question once and then come up with an appraoch. 
        # So one approach that comes to my mind when i see the qn is -> i will iterate nums and then there will be another iterations from i+1
        # and then say i call a function for counting the sum of digits for i and j and compare .
        # and tehen if they are equal i have a variablecalled say total which aadds these 2 and keeps track of max as well , and then i return total . 
        # This is the brute force approach that is coming to my mind, i can code this up 
        # total = 0 
        # maxi = -1

        # def countDigits(n) :
        #     sumi = 0
        #     while n > 0  :
        #         sumi = sumi + n%10
        #         n = n //10
        #     return sumi          

        # for i in range(len(nums)) : 
        #     for j in range(i+1, len(nums)) : 
        #         if countDigits(nums[i]) ==  countDigits(nums[j]) : 
        #             print(countDigits(nums[i]), countDigits(nums[j]))
        #             total = nums[i] + nums[j] 
        #             print(total )
        #             maxi = max(maxi, total)
        # return maxi
        # Now to think of the optimal approach, i could do 1 thing. so we need to cache or memoize the sum of digits 
        # because we are calling it so many times right. 
        # so i think i could u know first store the sum of all digits somewhere like in a list or dictonary and then if something seems equal i will add that element and return.
        def countDigits(n) :
            sumi = 0
            while n > 0  :
                sumi = sumi + n%10
                n = n //10
            return sumi  

        hmap = {}  #sum , number
        total = 0
        maxi = -1  
        for i in range(len(nums)) : 
            y = countDigits(nums[i])
            if y not in hmap :
                hmap[y] = nums[i]
            else : 
                total = nums[i] + hmap[y] 
                hmap[y] = max(nums[i], hmap[y])
                maxi = max(total, maxi)
        return maxi




        
         

            


               



        