class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        top = 0
        bottom = n-1 #2
        left, right = 0, n-1
        x = 1 
        while top <= bottom and left <= right : 
            for i in range(left, right+1): 
                matrix[top][i] = x
                x = x + 1
            top = top + 1 

            for i in range(top, bottom+1): 
                matrix[i][right] = x 
                x = x + 1
            right -= 1

            for i in range(right, left-1, -1): 
                matrix[bottom][i] = x 
                x = x + 1
            bottom -=1

            for i in range(bottom, top-1, -1): 
                matrix[i][left] = x 
                x = x + 1
            left = left + 1
        return matrix


        