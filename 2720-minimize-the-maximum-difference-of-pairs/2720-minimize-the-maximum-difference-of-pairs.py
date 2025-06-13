class Solution:
    def minimizeMax(self, nums, p):
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        result = float('inf')

        while left <= right:
            mid = (left + right) // 2
            if self.is_valid(nums, p, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def is_valid(self, nums, p, mid):
        count = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= mid:
                count += 1
                i += 2  # skip the next element
            else:
                i += 1
        return count >= p
