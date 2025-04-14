class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i*i for i in range(1, n+1)]
        sq_set = set(squares)
        
        ans = 0
        for i in range(n):
            for j in range(n):
                if squares[i] + squares[j] in sq_set: ans+=1
        return ans

# PLEASE UPVOTE IF HERE :)