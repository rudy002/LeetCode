class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        maxi = 0

        for num in nums:
            if num ==1:
                count+=1
                
            else:
                if count>maxi:
                    maxi = count
                    count = 0
                else:
                    count = 0
            if count>maxi:
                maxi = count

        
        
        return maxi