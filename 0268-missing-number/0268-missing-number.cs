public class Solution {
    public int MissingNumber(int[] nums) {
        for (int i = 0 ; i < nums.Length+1; i++) { 
            if ( !nums.Contains(i)){ 
                return i;
            }


        }
        return 0;
        
    }
}