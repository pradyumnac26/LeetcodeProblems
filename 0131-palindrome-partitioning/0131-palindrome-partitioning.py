class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindromeCheck(left, right) :
            while left <= right : 
                if s[left]!= s[right] : 
                    return False
                else : 
                    left = left + 1 
                    right = right -1
            return True  


        def backtrack(start_index, s, part, result) : 
            if start_index == len(s) : 
                result.append(list(part))
                return 
            for end_index in range(start_index, len(s)) : 
                if isPalindromeCheck(start_index, end_index) : 
                    part.append(s[start_index:end_index+1])
                    backtrack(end_index+1, s, part, result)
                    part.pop()

            


        result = [] 
        part = [] 
        backtrack(0, s, part, result)
        return result


        