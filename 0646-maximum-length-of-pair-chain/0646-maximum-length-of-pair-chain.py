class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cnt = 0
        one, two = pairs[0][0], pairs[0][1]
        x = []
        pairs.sort(key=lambda x: x[1])
        x.append(pairs[0])
        for i in range(1, len(pairs)) : 
            start, end = pairs[i][0], pairs[i][1]
            if x and start > x[-1][1] : 
                x.append([start, end])
                print(x)
        return len(x)
   






        