class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        x = [] 
        for i in responses : 
            x.append(list(set(i)))
        print(x)
        hmap = defaultdict(int) 
        for i in x : 
            for j in i : 
                hmap[j] +=1
        z = max(hmap.values())
        arr = [] 
        for k,v in hmap.items() : 
            if v == z : 
                arr.append(k)
        return min(arr)

        
        