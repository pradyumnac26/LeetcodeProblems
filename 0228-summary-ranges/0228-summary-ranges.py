class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] # [start, end] or [x, y]

        for n in nums : 
            if ranges and ranges[-1][1] == n-1 : 
                ranges[-1][1] = n 
            else : 
                ranges.append([n,n])
        result = [] 
        for x,y in ranges : 
            if x==y : 
                result.append(str(x))
            else : 
                result.append(f"{x}->{y}")
        return result


        



        