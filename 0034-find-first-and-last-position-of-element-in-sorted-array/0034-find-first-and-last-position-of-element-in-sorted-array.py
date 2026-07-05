class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_first(nums, target):

            l, r = 0, len(nums)-1
            result = -1

            while l<=r:
                mid = (l+r) // 2

                if nums[mid] > target:
                    r = mid -1
                elif nums[mid] < target: 
                    l = mid +1
                else: 
                    result = mid
                    r = mid -1

            return result

        def find_last(nums, target):
            l, r = 0, len(nums)-1
            result = -1

            while l<=r:
                mid = (l+r) // 2

                if nums[mid] > target:
                    r = mid -1
                elif nums[mid] < target: 
                    l = mid +1
                else: 
                    result = mid
                    l = mid +1
            
            return result

        
        first = find_first(nums, target)
        last = find_last(nums, target)


        return [first, last]