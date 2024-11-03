class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) : 
            return False 
        ss = s + s 
        if goal in ss : 
            return True 
        return False

        