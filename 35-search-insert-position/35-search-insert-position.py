class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        if target == nums[low]:
            return low
        elif target == nums[high]:
            return high
        else:
            while low <= high:
                mid = (low+high)//2
                
                if target == nums[mid]:
                    return mid
                
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return low