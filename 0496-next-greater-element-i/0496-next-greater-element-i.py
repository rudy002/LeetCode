class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = []
        
        for i in nums1:
            if i in nums2:
                index = nums2.index(i)

            for j in range(index + 1, len(nums2)):
                
                if nums2[j] > i:
                    ls.append(nums2[j])
                    break
            
            else:
                ls.append(-1)

        
        return ls
            

