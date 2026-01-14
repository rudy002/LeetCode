class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        
        while n != 1:
            n/=2
            if n<1:
                return False

        return True 