class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxNum1 = -2**31
        maxNum2 = -2**31
        maxNum3 = -2**31

        nums = list(set(nums))
        print(nums)
        
        if len(nums) in [1, 2]:
            return max(nums)
        elif len(nums) == 3:
            return min(nums)
        else:
                nums.remove(max(nums))
                nums.remove(max(nums))
                return max(nums)


       


       
