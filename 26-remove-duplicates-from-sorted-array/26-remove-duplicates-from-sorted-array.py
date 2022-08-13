class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_place = 1
        for pointer in range(1, len(nums)):
            if nums[pointer] != nums[pointer-1]:
                nums[to_place] = nums[pointer]
                to_place += 1
        return to_place
            