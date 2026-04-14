class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in index:
                return [i, index[complement]]
            
            index[num] = i