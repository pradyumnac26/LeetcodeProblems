class Solution:
    def findNumbers(self, nums: List[int]) -> int:


        def isEvenDigit(n): 
            count = 0 
            while n > 0 : 

                count = count + 1
                n = n // 10
            if count % 2 == 0: 
                return True
            else : 
                return False

        cnt = 0 
        for i in nums: 
            if isEvenDigit(i): 
                cnt = cnt + 1 
        return cnt





            
        