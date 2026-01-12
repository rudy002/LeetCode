class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dico = {}

        for i in range(len(nums)):
            if nums[i] in dico:
                if abs(dico[nums[i]] - i) <= k:
                    return True
                else:
                    dico[nums[i]] = i
            else:
                dico[nums[i]] = i
        
        return False