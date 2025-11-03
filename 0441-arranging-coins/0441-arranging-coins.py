class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count = 1
        j = 0

        while n>0:
            n = n - count
            count+=1
            if n>=0:
                j+=1
        
        return j
