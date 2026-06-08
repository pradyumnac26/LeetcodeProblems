class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [] 
        greater = [] 
        cnt = 0 
        res = [] 
        for i in nums : 
            if i < pivot : 
                less.append(i)
            elif i > pivot : 
                greater.append(i) 

            else : 
                cnt +=1 
        res.extend(less)
        for i in range(cnt): 
            res.append(pivot)
        res.extend(greater)
        return res
            



        