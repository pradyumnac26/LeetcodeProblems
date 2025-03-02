class Solution:
    def clearDigits(self, s: str) -> str:
        answer = [] 
        for char in s : 
            if char.isdigit() : 
                answer.pop()
            else : 
                answer.append(char)
        return "".join(answer)



        