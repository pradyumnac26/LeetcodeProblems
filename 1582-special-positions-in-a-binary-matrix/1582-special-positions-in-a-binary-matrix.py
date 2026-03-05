class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0 
        colCount = [0]*len(mat[0])
        rowCount = [0]*len(mat) 
        for i in range(len(mat)) : 
            for j in range(len(mat[0])) : 
                if mat[i][j] == 1 : 
                    rowCount[i] +=1 
                    colCount[j]+=1

        for i in range(len(mat)): 
            for j in range(len(mat[0])) : 
                if mat[i][j] == 1 : 
                    if rowCount[i] == 1 and colCount[j] == 1 : 
                        cnt+= 1 
        return cnt


        