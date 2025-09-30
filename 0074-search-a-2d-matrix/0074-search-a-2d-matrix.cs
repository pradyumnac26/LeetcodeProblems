public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        // each row sorted in increasing order; 
        // first of each row is greater than last row ka int 
        
        // flatten the matrix to 1D and then solve it. binary search way. 
        int m = matrix.Length; 
        int n = matrix[0].Length; 
        int l = 0 ; 
        int r = m*n-1; 
        while (l<=r) { 
            int mid = (l+r)/2; 
            int row = mid/n; 
            int col = mid%n;
            if (matrix[row][col] > target) { 
                r = mid -1 ;
            }
            else if(matrix[row][col] < target) { 
                l = mid + 1;
            }
            else { 
                return true;
            }

        }
        return false;
        
    }
}