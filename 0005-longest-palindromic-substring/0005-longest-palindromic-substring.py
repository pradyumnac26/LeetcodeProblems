class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        longest = 0

        # odd length
        for k in range(len(s)):
            i = k - 1
            j = k + 1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                curr = j - i + 1
                if curr > longest:
                    longest = curr
                    res = s[i:j+1]
                i -= 1
                j += 1

        # even length
        for k in range(len(s) - 1):
            i = k
            j = k + 1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                curr = j - i + 1
                if curr > longest:
                    longest = curr
                    res = s[i:j+1]
                i -= 1
                j += 1

        # if no length>=2 palindrome found, return any single char
        return res if res != "" else s[0]


        