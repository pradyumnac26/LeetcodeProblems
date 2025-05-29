class Solution:
    def trap(self, height: List[int]) -> int:
        # min(maxL, maxR) - height[i]
        n = len(height)
        leftMax = [0]*len(height)
        rightMax = [0]*n
        res = 0 
        leftMax[0] = height[0]
        for i in range(1,n): 
            leftMax[i] = max(leftMax[i-1], height[i])
        rightMax[n-1] = height[-1]
        for j in range(n-2, -1, -1): 
            rightMax[j] = max(rightMax[j+1], height[j])
        for i in range(n): 
            res = res + min(leftMax[i], rightMax[i]) - height[i]
        return res


        