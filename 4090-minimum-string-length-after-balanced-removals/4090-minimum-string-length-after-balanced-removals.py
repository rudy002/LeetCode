class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        
        countA = s.count('a')
        countB = s.count('b')

        return abs(countA - countB)