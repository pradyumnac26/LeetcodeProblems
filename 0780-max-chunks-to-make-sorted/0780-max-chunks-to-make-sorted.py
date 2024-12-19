class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = 0 
        cnt = 0 
        for i in range(len(arr)) : 
            max_seen = max(max_seen, arr[i])
            if i == max_seen : 
                cnt +=1 
        return cnt


        