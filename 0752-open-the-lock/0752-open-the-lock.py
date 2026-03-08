class Solution:
    def openLock(self, deadends: List[str], target: str) -> int: 
        
        q = deque([("0000", 0)])
        s = set(deadends) 
        vis = set()
        vis.add("0000")
        if "0000" in s : 
            return -1
        while q : 
            start, dist = q.popleft() 
            if start == target : 
                return dist 
            for i in range(4) :
                digit = int(start[i]) 
                add = start[:i]+str((digit+1)%10) + start[i+1:] 
                sub = start[:i] + str((digit-1+10)%10) + start[i+1:] 
                if add not in s and add not in vis : 
                    vis.add(add)
                    q.append((add, dist+1))
                if sub not in s and sub not in vis: 
                    vis.add(sub)
                    q.append((sub, dist+1)) 
        return -1



        