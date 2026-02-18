class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sorting 
        cnt = Counter(nums) # {1 : 4 , 2 : 4, 3 : 2 }
        buckets = [[] for _ in range(max(cnt.values())+1)]  

        print(buckets)
        for key,v in cnt.items() :
            buckets[v].append(key)
        print(buckets)
        res = [] 
        for i in range(len(buckets)-1, 0, -1) : 
            for j in buckets[i] : 
                res.append(j)
                if len(res) == k : 
                    return res
