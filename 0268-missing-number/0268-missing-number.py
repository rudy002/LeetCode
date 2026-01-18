class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        total1 = sum(nums)
        total2 = 0

        for i in range(len(nums)+1):
            total2 += i

        return total2 - total1
        