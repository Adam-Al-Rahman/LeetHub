class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        for i in range(len(nums)):
            total -= nums[i]
            if (left == total):
                return i
            left += nums[i]
        return -1
            
        