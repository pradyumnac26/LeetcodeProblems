class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        i = 0
        score = 0 
        seen = set()

        while 0<=i <len(instructions):
            if i in seen:
                break
            seen.add(i)
            if instructions[i] == "jump": 
                i = i+values[i]
            elif instructions[i] == "add" : 
                score = score + values[i]
                i = i+1

        return score

        