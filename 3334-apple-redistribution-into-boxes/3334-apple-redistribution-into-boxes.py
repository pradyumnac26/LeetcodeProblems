class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        c = sorted(capacity, reverse = True)
        cnt = 0 
        for i in c : 
            s = s - i
            cnt = cnt + 1  
            if s<=0:
                return cnt


        return cnt
            
        