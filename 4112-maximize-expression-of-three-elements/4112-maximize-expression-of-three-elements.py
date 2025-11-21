class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        
        max_val1 = max(nums)
        min_val = min(nums)

        tempList = nums.copy()
        tempList.remove(max_val1)
        max_val2 = max(tempList)

        return max_val1 + max_val2 - min_val