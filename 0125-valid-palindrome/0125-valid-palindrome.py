class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in s:
            if i.isalnum():  # Accept both letters and digits
                x += i.lower()
        return x == x[::-1]
