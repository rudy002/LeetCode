class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        suite = []
        result = []

        if not nums:
            return result

        for i in range(len(nums)):
            if i == 0:
                suite.append(nums[i])
                continue

            # suite continue
            if nums[i] - 1 == nums[i-1]:
                suite.append(nums[i])

            # suite cassée
            else:
                if len(suite) > 1:
                    result.append(str(suite[0]) + "->" + str(suite[-1]))
                else:
                    result.append(str(suite[0]))

                suite.clear()
                suite.append(nums[i])   # ✅ redémarre la nouvelle suite

        # ✅ flush la dernière suite
        if len(suite) > 1:
            result.append(str(suite[0]) + "->" + str(suite[-1]))
        else:
            result.append(str(suite[0]))

        return result
