class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # so we need to return an index here, and we have to return only when we split the array into 2 elements, then both the arrays should hav the same dominant element. 
        # if its not possible have to return -1. 
        # so i need to keep track of the freq of the elements wih indexes. of the most frequently ocurred. 
        # so say first i get the mst dominant element oif the entire array say for [1,2,2,2] it is 2.
        # and then i get now i need to keep. track at each iterations. 
        # so thw dominant elements means which are present more than the this is more thn half the elements in the spplit array. 
        # say i write a func to find the dominnant element , if count(x) > len(arr)/2 then return i else false.
        # now have to check this at every index , so for i in r nums : 1, 2, ,2 . 


        dom, occ = Counter(nums).most_common(1)[0]
        cnt  = 0 
        print(dom, occ)
        if occ <= len(nums)//2 : 
            return -1
        for i in range(len(nums)) : 
            if nums[i] == dom : 

                cnt = cnt + 1 
                print(cnt)
                if cnt <= occ and cnt > (i+1)//2 and (occ-cnt) > (len(nums)-i-1)//2:
                    return i 
        return -1  


        
            
         
        
        



        