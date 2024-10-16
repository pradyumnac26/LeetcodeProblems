class Solution:
    def reorganizeString(self, s: str) -> str:
        res = "" 
        maxHeap = [] 
        count = Counter(s)
        for char, cnt in count.items() : 
            heapq.heappush(maxHeap, (-cnt, char))
        prev_char = None
        prev_count = 0 

        while maxHeap : 
            cnt, char = heapq.heappop(maxHeap)
            res = res + char 
            if prev_count < 0 : 
                heapq.heappush(maxHeap, (prev_count, prev_char )) 
            
            prev_char = char 
            prev_count = cnt + 1
            
        
        if len(res) != len(s) : 
            return "" 
        return res






        
        