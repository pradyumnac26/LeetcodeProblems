from typing import List
from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])


        diag = []                          
        lower = defaultdict(list)          
        upper = defaultdict(list)          

        for i in range(m):
            for j in range(n):
                if i == j:
                    diag.append(grid[i][j])
                elif i > j:
                    lower[i - j].append(grid[i][j])
                else:
                    upper[i - j].append(grid[i][j])


        diag.sort(reverse=True)                
        for k in lower: lower[k].sort(reverse=True)  
        for k in upper: upper[k].sort()              

        d = 0
        li = {k: 0 for k in lower}
        ui = {k: 0 for k in upper}

        for i in range(m):
            for j in range(n):
                if i == j:
                    grid[i][j] = diag[d]; d += 1
                elif i > j:
                    k = i - j
                    grid[i][j] = lower[k][li[k]]
                    li[k] += 1
                else:
                    k = i - j
                    grid[i][j] = upper[k][ui[k]]
                    ui[k] += 1

        return grid
