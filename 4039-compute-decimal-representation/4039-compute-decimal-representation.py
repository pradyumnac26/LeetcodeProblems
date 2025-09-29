class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # 500, 30, 7 are base-10 component means 
        # say i have 537, then 10**2 x 5, 10**1*3 10*0 x 7
        # 537/10 = 53/10 = 5 /10 = 0 
        res = []
        mul = 0 
        while n : 
            x = n %10
            if x != 0 : 
                res.append(x*(10**mul))          
            mul = mul+1
            n = n//10
        return res[::-1]


            

        