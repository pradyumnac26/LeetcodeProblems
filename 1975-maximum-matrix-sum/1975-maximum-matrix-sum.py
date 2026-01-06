class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int: 
        n, m = len(matrix), len(matrix[0])
        cnt = 0 
        sumi = 0 
        mini = float('inf')
        for i in range(n): 
            for j in range(m): 
                sumi = sumi + abs(matrix[i][j])
                mini = min(abs(matrix[i][j]), mini)
                if matrix[i][j] < 0 : 
                    cnt +=1 
        if cnt % 2 == 0 : 
            return sumi 
        else : 
            return sumi - 2*mini

        



        

        