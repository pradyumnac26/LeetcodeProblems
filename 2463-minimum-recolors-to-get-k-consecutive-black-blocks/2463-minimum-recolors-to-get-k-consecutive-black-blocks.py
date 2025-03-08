class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0 , 0
        count = 0 
        mini = float("inf")
        while (right < len(blocks)) : 
            if blocks[right] == 'W' : 
                count = count + 1
            if right - left + 1 == k : 
                mini = min(mini, count)
                if blocks[left] == 'W' : 
                    count = count -1 
                left = left + 1 
            right = right + 1 
        return mini
            



        
        