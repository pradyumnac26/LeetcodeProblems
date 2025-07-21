class Solution:
    def checkDivisibility(self, n: int) -> bool:

        def calculate(n) :
            sumi = 0 
            prod = 1 
            while n : 
                dig = n%10
                sumi = sumi + dig
                prod = prod*dig
                n =  n//10
            return (sumi, prod)

        x, y = calculate(n)
        add = x + y 
        return True if n%add == 0 else False


        