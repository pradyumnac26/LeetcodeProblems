from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        result = []
        stack = []
        min_char = 'a'

        for char in s:
            stack.append(char)
            count[char] -= 1

            # Find the smallest character still left in the string
            while count[min_char] == 0 and min_char < 'z':
                min_char = chr(ord(min_char) + 1)

            # Pop from stack while top is <= current smallest remaining character
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        return ''.join(result)
