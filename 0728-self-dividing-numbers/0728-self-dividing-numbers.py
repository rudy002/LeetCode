class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        for i in range(left, right+1):
            digits = list(map(int, str(i)))
            
            valid = True
            for d in digits:
                if d == 0 or i % d !=0:
                    valid = False
                    break
                
            if valid:
                res.append(i)
                

        return res    