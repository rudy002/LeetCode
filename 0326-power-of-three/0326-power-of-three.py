class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # utiliser le plus grand nombre des int et le diviser par n (a test parce que pas sur)
        if n == 0:
            return False
        elif n < 0:
            return False
        
        if 1162261467 % n == 0:
            return True
        else:
            return False


        
