class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        if n%2 == 0:
            
            array_output = list(range(-n//2, 0))
            array_output.extend(range(1, n//2 + 1))
        else:
            array_output = list(range((-n//2)+1, 0))
            array_output.extend(range(0, n//2 + 1))
            
        
        
        return array_output
