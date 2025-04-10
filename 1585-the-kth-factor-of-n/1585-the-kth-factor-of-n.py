class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # factors are those n%i == 0 , then i is a factor, so 
        # say if i say 36 the factors are -> [1,2,3,4,6,9,12,18,36]
        # 1x36, 36x1,2x18, 18x2, 3x12,12x3,4x9, 9x4, 6x6
        x = [] 
        for i in range(1, int(sqrt(n)) + 1) : 
            if n%i == 0: 
                x.append(i)
                if n//i != i: 
                    x.append(n//i)
        x.sort()
        if k <= len(x):
            return x[k - 1]
        return -1

             


        