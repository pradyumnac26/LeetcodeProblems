class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x = [0]*len(indices)
        for i in range(len(indices)):
            x[indices[i]] = s[i]
        return "".join(x)


        