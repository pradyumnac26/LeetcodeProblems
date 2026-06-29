class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set() 
        nums.sort()

        def dfs(i) : 
            if i >= len(nums) : 
                res.add(tuple(st)) 
                return


            st.append(nums[i])
            dfs(i+1)
            st.pop() 
            dfs(i+1)

        st = [] 
        dfs(0)
        return list(res)
        
        