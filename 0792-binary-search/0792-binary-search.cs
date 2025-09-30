public class Solution {
    public int Search(int[] nums, int target) {
        Array.Sort(nums);
        int low = 0 ; 
        int high = nums.Length-1; 
        while (low <= high) { 
                int mid = (low + high)/2;
                if (nums[mid] > target) { 
                    high = mid -1;

                }
                else if (nums[mid] < target) { 
                    low = mid+1;
                }
                else { 
                    return mid;
                }
        }
        return -1;
    }
}