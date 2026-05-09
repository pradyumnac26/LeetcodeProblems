class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        res = [] 
        for i in range(len(strs)): 
            word = strs[i]
            s = "".join(sorted(word)) 
            hmap[s].append(strs[i])
        
        for v in hmap.values() : 
            res.append(v)
        return res
        
        