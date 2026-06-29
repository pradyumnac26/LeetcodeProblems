class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(i) :
            if i >= len(nums) : 
                res.append(st[:])
                return 

            st.append(nums[i])
            dfs(i+1) 
            st.pop()
            dfs(i+1)

            


        st = [] 
        dfs(0) 
        return res

        