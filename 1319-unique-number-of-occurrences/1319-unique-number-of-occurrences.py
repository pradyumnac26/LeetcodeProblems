class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x = Counter(arr)
        y = [] 
        for i,j in x.items() : 
            if j not in y : 
                y.append(j)
            else : 
                return False
        return True
            

        