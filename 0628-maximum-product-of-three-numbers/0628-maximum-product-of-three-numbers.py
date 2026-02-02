class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        total1 = 1
        total2 = 1

        for i in range(len(nums)-3, len(nums), 1):
            total1 *= nums[i]

        nums.append(nums[0])
        nums.append(nums[1])

        for i in range(len(nums)-3, len(nums), 1):
            total2 *= nums[i]

        return max(total1, total2)
        