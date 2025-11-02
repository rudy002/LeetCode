# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n

        while (low<=high): 
            
            pick = (low+high)//2
            
            if (guess(pick) ==1):
                low = pick + 1
            elif (guess(pick) ==-1):
                high = pick
            elif (guess(pick == 0)):
                return pick
        
            ##  1 2 3 4 5 6 7 8 9 10