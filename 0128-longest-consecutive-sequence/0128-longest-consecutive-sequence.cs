public class Solution {
    public int LongestConsecutive(int[] nums) {
        Array.Sort(nums); 
        int cnt =1;
        int longest = 1 ;
        if (nums.Length == 0) { 
            return 0;
        } 
        for (int i = 1 ; i < nums.Length; i++) { 
            if (nums[i] == nums[i-1]) { 
                continue;
            }
            if (nums[i] - nums[i-1]  == 1 ) { 
                cnt+=1 ;
            }
            else { 
                cnt = 1;
            }
            longest = Math.Max(cnt, longest);

            
        }
        return longest;

        
    }
}