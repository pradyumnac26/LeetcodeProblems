public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        Array.Sort(strs); 
        Console.WriteLine(string.Join(", ", strs));
        string first = strs[0];
        string last = strs[^1];
        string x = "";
        int mini = Math.Min(first.Length, last.Length);
        for (int i = 0 ; i < mini; i++) {
            if (first[i] == last[i]) { 
                x = x + first[i];
            }
            else { 
                break;
            }

        }
return x;        
        
    }
}