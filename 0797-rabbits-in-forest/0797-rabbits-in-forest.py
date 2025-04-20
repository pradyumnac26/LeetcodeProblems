class Solution:
    def numRabbits(self, a: List[int]) -> int:
        return sum(ceil(f/(v+1))*(v+1) for v,f in Counter(a).items())