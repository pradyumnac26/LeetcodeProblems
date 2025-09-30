public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> dict = new Dictionary<char, int>();
        foreach (char c in s) { 
            dict[c] = 1 + dict.GetValueOrDefault(c, 0) ; 
        }
        foreach (char c in t) { 
            if (!dict.ContainsKey(c)) return false; 
            dict[c] = dict[c] -1 ;
        }

        foreach (var kvp in dict) { 
            if (kvp.Value !=0) { 
                return false;
            }
        }

        return true;
       


        
    }
}