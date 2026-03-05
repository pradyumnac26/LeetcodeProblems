class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = [0]*len(grid) 
        onesCol = [0]*len(grid[0]) 
        zerosRow = [0]*len(grid) 
        zerosCol = [0]*len(grid[0])
        diff = [[0]*len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1 : 
                    onesRow[i] += 1
                    onesCol[j] += 1 
                else : 
                    zerosRow[i] += 1 
                    zerosCol[j] += 1 
        for i in range(len(grid)) : 
            for j in range(len(grid[0])): 
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j] 
        return diff

        