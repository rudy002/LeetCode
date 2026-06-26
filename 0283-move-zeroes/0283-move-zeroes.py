class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for l in range(len(nums)):
            if nums[l] != 0:
                nums[l], nums[insert_pos] = nums[insert_pos], nums[l]
                insert_pos += 1

    