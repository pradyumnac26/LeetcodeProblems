class Solution:
    def countLargestGroup(self, n: int) -> int:

        def count_digit_sum(k):
            sumi = 0 
            while k > 0 : 
                sumi = sumi + k%10
                k = k//10
            return sumi
        

        hmap = defaultdict(int)
        sum_of_n = 0 
        count = 0
        for i in range(1, n+1): 
            sum_of_n = count_digit_sum(i)
            hmap[sum_of_n] +=1
        max_val = max(hmap.values())
        print(max_val)
        for k,v in hmap.items(): 
            if v == max_val : 
                count = count +1
                print(k,v,count)
        return count 
        

        

        