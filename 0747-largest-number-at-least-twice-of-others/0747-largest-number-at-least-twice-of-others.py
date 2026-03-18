class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_index = nums.index(max_num)

        print("max number : ", max_num, " and max index : ", max_index)

        for i in nums:
            if i != max_num and 2*i > max_num:
                return -1
        
        return max_index