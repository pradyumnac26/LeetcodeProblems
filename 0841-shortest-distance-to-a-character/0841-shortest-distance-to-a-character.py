class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [0]*len(s)
        pointers = [] 
        for i in range(len(s)): 
            if s[i] == c : 
                pointers.append(i)
        print(pointers) 
        j = 0 
        for i in range(len(s)): 
            while j < len(pointers) - 1 and abs(pointers[j+1] - i) <= abs(pointers[j] - i):
                j += 1
            ans[i] = abs(pointers[j] - i )

        return ans

        