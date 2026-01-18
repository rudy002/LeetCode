# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        

        # verification du cas ou il y a juste 1 element    
        if n == 1:
            return n
        

        while left <right:
            if isBadVersion(left + math.floor((right-left)/2)):
                right = math.floor(left + (right-left)/2)
                
                if not isBadVersion(right-1):
                    return right
            
            else:
                left = math.floor(left + (right-left)/2)

                if isBadVersion(left+1):
                    return left+1


            
    