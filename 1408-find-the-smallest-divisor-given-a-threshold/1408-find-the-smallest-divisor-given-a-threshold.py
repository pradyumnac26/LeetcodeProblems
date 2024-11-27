class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        if len(nums) > threshold : 
            return -1
        def ByDiv(arr, div) : 
            div_sum = 0 
            n = len(arr)
            for i in range(n) : 
                div_sum += math.ceil(arr[i]/div)
            return div_sum

        while low <= high : 
            mid = (low + high) // 2 
            x = ByDiv(nums, mid)
            if x <= threshold : 
                high = mid -1 
            else : 
                low = mid+1
        return low 
    



        