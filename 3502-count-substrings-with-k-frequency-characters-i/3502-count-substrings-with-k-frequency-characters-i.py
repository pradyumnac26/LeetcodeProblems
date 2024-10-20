from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        total_count = 0
        freq = defaultdict(int)
        start = 0
        
        # Expand the window by moving the `end` pointer
        for end in range(len(s)):
            # Add current character to the frequency map
            freq[s[end]] += 1
            
            # Shrink the window from the left (move `start` pointer)
            # until the window becomes invalid
            while any(count >= k for count in freq.values()):
                # For each valid window, count all substrings ending at `end`
                total_count += len(s) - end
                # Reduce the frequency of the character at `start` and move `start`
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
        
        return total_count
