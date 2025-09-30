public class Solution {
    public int LengthOfLongestSubstring(string s) {
        Dictionary<char, int> hmap = new Dictionary<char, int>();
        int l = 0 ; 
        int r = 0 ; 
        int maxi = 0;
        while (r < s.Length) { 
            hmap[s[r]] = hmap.GetValueOrDefault(s[r], 0) + 1 ; 
            while (hmap[s[r]] > 1) { 
                hmap[s[l]]-=1;
                if (hmap[s[l]] == 0) { 
                    hmap.Remove(s[l]);
                }
                l = l + 1 ;
            }
            maxi = Math.Max(maxi, r-l+1); 
            r = r + 1;
            
        }
        return maxi;
        
    }
}