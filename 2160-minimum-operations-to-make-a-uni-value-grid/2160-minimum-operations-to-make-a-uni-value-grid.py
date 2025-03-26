class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # so how to decide whih number to converge at ? 
        # we need to find the min operation. bfs problem ? 
        # Can be done more than once ?
        # say i have grid[0][0], and i have 2 choices add x or subtract x , and have the same 2 choices for grid[0][1] and so on. 
        # after that we check the netire array and make them vomenear , so we can converge on the midpoint like after sorting. 
        # so say i convert this 2D array to a 1D array and then do bs find the mid and subtract alll elements from the mid and keep track of minop. 
        # lets try this approach , not a O(N^2 ) i think for sure., but extra space yes 

        z = []
        for i in grid : 
            for j in i : 
                z.append(j)

    
        base = z[0]
        for val in z:
            if (val - base) % x != 0:
                return -1

        z.sort()
        length = len(z)
        print(z)
        mid = (length - 1 )//2
        op = 0
        for i in range(len(z)):
            op = op + abs((z[mid] - z[i])//x)
            
        return op



        