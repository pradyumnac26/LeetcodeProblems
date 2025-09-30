public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> hmap = new Dictionary<int, int>();
        int[] res = new int[2];
        for (int i = 0 ; i < nums.Length; i++) { 

            int find = target - nums[i] ;
            if (hmap.ContainsKey(find)) { 
                res[0] = hmap[find];
                res[1] = i;
                return res;
            }
            hmap[nums[i]] = i ; 
        }
        return null;
        
    }
}