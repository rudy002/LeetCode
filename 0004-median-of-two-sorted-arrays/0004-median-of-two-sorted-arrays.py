class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        res = []
        pointer1, pointer2 = 0, 0

        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                res.append(nums1[pointer1])
                pointer1+=1
            else: 
                res.append(nums2[pointer2])
                pointer2+=1
        
        res.extend(nums1[pointer1:])
        res.extend(nums2[pointer2:])

        return (res[(len(res) - 1) // 2] + res[len(res) // 2]) / 2