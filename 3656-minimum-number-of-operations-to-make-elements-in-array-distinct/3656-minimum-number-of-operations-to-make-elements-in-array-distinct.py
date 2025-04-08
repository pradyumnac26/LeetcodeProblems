class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # have to remove the first 3 elements of an array until there are no duplicates of values in the array. 
        # so how to check if there are duplicates in an array ? 
        # Run a counter every time we make a change and then if cnt[val] == 2? 
        # so brute force would be - say i count and put the val, cnt in hmap
        # and then i seee if any val has cnt >1 then i call another function.
        # and maybe that function would reduce the array by 3 by remove the first 3 elements., and then we need to run this for loop on that updated x.
        # counter , any value more than 3 elements ? okay , remove first 3 elements,
        # again run counter, any value more than 3 ? okay remove frist 3 elements.
        # again ru n counter, no value more than 3 ? then return cnt.

        def count(x) : 
            for i, v in Counter(x).items() : 
                if v > 1 : 
                    return True
            return False

        x = nums[:]
        cnt = 0
        while count(x) :
            if len(x) < 3 : 
                cnt = cnt + 1
                return cnt

            x = x[3:]
            cnt = cnt +1
        return cnt
            
        


        

        