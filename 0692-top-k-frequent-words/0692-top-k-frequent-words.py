class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        buckets = [[] for _ in range(len(words)+ 1)]
        x = Counter(words)
        for key,v in x.items(): 
            buckets[v].append(key)
        print(buckets)

        res = [] 
        for i in range(len(buckets)-1, -1, -1): 
            for j in sorted(buckets[i]): 
                res.append(j)
                if len(res) == k : 
                    return res


        