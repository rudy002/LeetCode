class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j+1
                right = len(nums) - 1
                while left<right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] <target:
                        left +=1
                    else:
                        result.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right -= 1

        return list(result)