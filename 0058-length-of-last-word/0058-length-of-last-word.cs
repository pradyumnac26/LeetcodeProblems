public class Solution {
    public int LengthOfLastWord(string s) {
        String[] str = s.Trim().Split();
        foreach(string a in str) { 
            Console.WriteLine(a);
        }
        return str[str.Length-1].Length;
        
    }
}