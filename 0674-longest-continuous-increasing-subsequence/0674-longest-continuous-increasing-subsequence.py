class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_seq = 0
        seq = 0
        prev = -10**9

        for i in nums:
            if i > prev:
                prev = i
                seq +=1
            else:
                if seq > max_seq:
                    max_seq = seq
                seq = 1
                prev = i
        
        if seq > max_seq:
            max_seq = seq
        return max_seq
                
