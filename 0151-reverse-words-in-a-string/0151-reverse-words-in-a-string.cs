public class Solution {
    public string ReverseWords(string s) {
        String[] str = s.Trim().Split(' ', StringSplitOptions.RemoveEmptyEntries);
        string x = "" ; 
        foreach(string i in str) { 
            x = i + " " + x;
        }
        return x.Trim();


        
    }
}