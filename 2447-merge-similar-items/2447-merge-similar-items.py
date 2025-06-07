class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hmap = defaultdict(list)
        ans = []
        for i in range(len(items1)): 
            hmap[items1[i][0]].append(items1[i][1])
        
        for i in range(len(items2)): 
            hmap[items2[i][0]].append(items2[i][1])
        print(hmap)

        for k, v in hmap.items(): 
            ans.append([k, sum(v)])
        
        return sorted(ans) 



        
        