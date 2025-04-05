class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # say we have [5,1,6] -> subsets are [5],[1], [6], [5,1], [5,6], [5,1,6] -> 5 + 1 + 6 + 4 + 3 + 7+2 = 28
        # 5, [5,1],[5,6] [5,1,6], [1], [1,6], [6]
        # xor of single elements would be them itself, and exour of 5,1 we could do. and xor
        # 1. 5, 2. 5^1, 3. 5^1^6, 4. 5^1^6^5 -> [1,6], 5^1^6^5^1 - > [6], 5^1^6^5^1^6 -> 0,
        # 5^1^6 -> 1^6 , 5^1^6^1 -> 5^6 , 5^1^6^6 -> 5^1, 5^1^6^5^6
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







        




        