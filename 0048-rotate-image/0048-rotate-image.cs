public class Solution {
    public void Rotate(int[][] matrix) {
        // transpose and then reverse. 
        for (int i = 0 ; i < matrix.Length ; i ++ ) { 
            for (int j = i+1 ; j < matrix.Length; j++) {
                int temp = matrix[i][j]; 
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp; 

            }
        }

        for (int i = 0 ; i < matrix.Length; i ++) { 
            Array.Reverse(matrix[i]);


        }
    }
}