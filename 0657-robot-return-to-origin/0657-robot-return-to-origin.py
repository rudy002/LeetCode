class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        count = {"R":0, "L":0 , "U":0 , "D": 0}

        for i in moves:
            count[i]+=1
        
        if (count["R"] - count["L"] == 0) and (count["U"] - count["D"] == 0):
            return True
        else:
            return False


    