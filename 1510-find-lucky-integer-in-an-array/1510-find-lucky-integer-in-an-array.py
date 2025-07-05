class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x = Counter(arr)
        maxi = -1
        for k,v in x.items() : 
            if k == v : 
                maxi = max(maxi, k)
        return maxi
                
        