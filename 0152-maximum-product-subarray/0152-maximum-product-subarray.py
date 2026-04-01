class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftProduct = 1
        rightProduct = 1
        ans = nums[0]
        n = len(nums)

        for i in range(n):
            if leftProduct == 0:
                leftProduct = 1
            if rightProduct == 0:
                rightProduct = 1

            leftProduct *= nums[i]
            rightProduct *= nums[n - 1 - i]

            ans = max(ans, leftProduct, rightProduct)

        return ans