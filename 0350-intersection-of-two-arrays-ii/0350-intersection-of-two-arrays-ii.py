class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        if len(nums1) > len(nums2):
            tab1 = nums1
            tab2 = nums2
        else:
            tab1 = nums2
            tab2 = nums1
        
        for i in tab1:
            if i in tab2:
                res.append(i)
                tab2.remove(i)
        
        return res
        