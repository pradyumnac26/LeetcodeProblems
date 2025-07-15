class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        x = {} 
        for i, ch in enumerate(s): 
            if ch not in x : 
                x[ch] = i 
            else : 
                x[ch] = i - x[ch] -1
        
        for i in range(26): 
            if distance[i]!=0 and chr(97+i) not in s : 
                continue
            if s.count(chr(97+i)) == 2: 
                if distance[i] != x[chr(97+i)]:
                    return False
        return True
        
        