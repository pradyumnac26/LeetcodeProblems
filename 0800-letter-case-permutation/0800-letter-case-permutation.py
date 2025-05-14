class Solution:
    def letterCasePermutation(self, s):
        res = []
        n = len(s)

        def backtrack(index, path):
            if index == n:
                res.append(path)
                return

            char = s[index]
            if char.isalpha():
                backtrack(index + 1, path + char.lower())
                backtrack(index + 1, path + char.upper())
            else:
                # Only one choice for digit
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return res
