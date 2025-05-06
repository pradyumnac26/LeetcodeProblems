class Solution:
    def maxProduct(self, n: int) -> int:
        x = [] 
        for i in str(n): 
            x.append(int(i))
        print(x)
        max_prod = -1
        for i in range(len(x)): 
            prod = x[i]
            for j in range(i+1, len(x)): 
                y =  prod*x[j]

                max_prod = max(max_prod, y)
        return max_prod


        