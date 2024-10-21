class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            # If we reach the end of the string, return 0
            if start == len(s):
                return 0
            
            max_splits = 0
            
            # Try splitting the string at every possible point
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the current substring is unique (not seen before)
                if substring not in seen:
                    seen.add(substring)  # Mark this substring as used
                    
                    # Recurse on the remaining part of the string
                    max_splits = max(max_splits, 1 + backtrack(end, seen))
                    
                    seen.remove(substring)  # Backtrack: remove the substring from the seen set
            
            return max_splits
        
        # Start backtracking from the first character with an empty set for seen substrings
        return backtrack(0, set())

# E