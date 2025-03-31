class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # so here - we can do either using stack or count i believe.
        # i can start with stack based solution. 
        # lets go through the dry run , so first it gors to stack and so if there i a mtching closing brackrt we pop the open bracket. and increase the count by 2. and return the cnt .
        # or len(s) - len(stack ) ->  would give us the valid parentheiss, but we also want the longest, so we could keep trac of the maxi i guess.
        # )()())
        # anothe eexample (())))()(()), so as its a substring , we need to find the longest contiguous. 

        stack = [-1]
        max_count = 0
        for i,ch in enumerate(s) : 
            if ch == '(' : 
                stack.append(i)
            else : 
                stack.pop()
                if stack : 
                    max_count = max(max_count, i - stack[-1])
                else : 
                    stack.append(i)
        return max_count 


        
            

        