class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Given nums, my task is to find an which has most occurences, and then find an element which is lesser than that element. 
        # so say 5 has duplicates , then the previous greater element is 4, so 4 is a valid integer , so take 4 all 5s and convert them to 4s. 
        # so itll become [2,4,4,4,4], now again repeat the same, find duplicates and then find the previous greater element, and then change all duplicate elements to that valid previous greater.
        # also after each iteration check if each element in the arrray is equal to the given value k, if yes then return the min cnt, else return -1
        # hope i am on the righvttrack.
        st = set()
        for x in nums : 
            if x < k : 
                return -1
            elif x > k : 
                st.add(x)
        return len(st)


        
        