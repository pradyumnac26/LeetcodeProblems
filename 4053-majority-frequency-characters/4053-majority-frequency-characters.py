class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        x = Counter(s)
        # {a:3, b:3, c:2, d:4, e:1}
        n = max(x.values()) +1 

        bucket = [[] for _ in range(n)]
        for k,v in x.items() : 

            bucket[v].append(k)
        maxi = 0 
        print(bucket)
        for i in range(len(bucket)-1, -1, -1): 
            if maxi < len(bucket[i]) : 
                maxi = len(bucket[i]) 
                x = "".join(bucket[i])
        return x
        


        