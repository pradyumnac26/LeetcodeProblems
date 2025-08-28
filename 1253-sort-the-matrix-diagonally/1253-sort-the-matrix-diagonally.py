class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diag = defaultdict(list)
        for i in range(len(mat)): 
            for j in range(len(mat[0])): 
                diag[i-j].append(mat[i][j])
        for i in diag : 
            diag[i].sort()
        print(diag)

        ptr = {k : 0 for k in diag}
        
        for i in range(len(mat)): 
            for j in range(len(mat[0])):
                k = i - j  
                mat[i][j] = diag[k][ptr[k]]
                ptr[k] +=1 
        return mat

        