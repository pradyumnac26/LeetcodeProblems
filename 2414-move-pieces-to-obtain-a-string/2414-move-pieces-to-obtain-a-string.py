class Solution:
    def canChange(self, start: str, target: str) -> bool:

        if start.replace("_", "") != target.replace("_","") : 
            return False

        n = len(start)
        start_idx = 0
        target_idx = 0 

        while start_idx < n and target_idx < n :
            while start_idx < n and start[start_idx] == "_" : 
                start_idx += 1 
            while target_idx < n and target[target_idx] == "_" : 
                target_idx += 1 

            if start_idx < n and target_idx < n:
                if start[start_idx] == 'L' and start_idx < target_idx:
                    return False
                if start[start_idx] == 'R' and start_idx > target_idx:
                    return False
            start_idx +=1
            target_idx +=1
        return True

                
            

        
        