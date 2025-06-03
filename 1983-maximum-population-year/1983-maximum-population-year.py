class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # [1950, 1961], [1960, 1971] - cnt = 2 as they are overlaping. , for the next set , again its 2 ppl so  max is 2 and the first year of that is 1960
        starts = []
        ends = [] 
        for x,y in logs : 
            starts.append(x)
            ends.append(y)
        starts.sort()
        ends.sort()
        print(starts, ends)
        i, j = 0, 0
        res, cnt = 0, 0 
        while i < len(starts) and j < len(ends): 
            if starts[i] < ends[j] :
                cnt = cnt + 1 
                if cnt > res : 
                    res = cnt 
                    year = starts[i]
                i = i + 1
            else : 
                cnt = cnt - 1
                j = j + 1

        return year
            

        