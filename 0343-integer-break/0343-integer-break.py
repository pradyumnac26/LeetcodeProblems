class Solution:
    def integerBreak(self, n: int) -> int:
        # we know that 2 can be broken down as 2 ones so product is 1
        # and 3 can be broken down into 1+1+1, but product is 1, so 2+1 so product is 2
        #  4 can be broken down into 2+2, 3+1, 2+1+1 -> max is 4
        # 5 can be -> 3+2, 4+1, max is 6 
        # 6 is 3+3, 4+2 -> 9
        # 7 is 4+3 = 12
        # 8 is 3+3+2 = 16
        # 9 is 3+3+3 = 27
        # 10 is 36
    # 1, 1, 2, 4, 6, 9, 12, 16, 20, 36
        if n == 2 : 
            return 1
        if n == 3 : 
            return 2
        count , rem = divmod(n,3)
        if rem == 0 : 
            return 3**count
        if rem == 1 : 
            return 3**(count -1) *4
        else : 
            return 3**count *2



        