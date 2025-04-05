class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def generate_subsets(i, x):
            if i == len(nums): 
                subsets.append(x[:])
                return
            
            x.append(nums[i])
            generate_subsets(i+1, x)
            x.pop()
            generate_subsets(i+1, x)


        subsets = [] 
        x = [] 
        total = 0
        generate_subsets(0, x)
        print(subsets)
        for i in subsets: 
            sub_total = 0
            for j in i :
                sub_total = sub_total^j
            total = total + sub_total
        return total







        




        