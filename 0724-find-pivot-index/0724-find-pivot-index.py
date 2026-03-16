class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        sum_left = 0
        sum_right = sum(nums[1:])

        while index< len(nums):
            if sum_left == sum_right:
                return index
            
            sum_left+= nums[index]
            index+=1
            if index < len(nums):
                sum_right-= nums[index]


        return -1