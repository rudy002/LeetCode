class Solution:
    def addDigits(self, num: int) -> int:
        
        def process(self, x:int) ->int:
            digit = []
            while x > 0:
                digit.append(x%10)
                x //= 10
                digit.reverse()
            return sum(digit)
                
        
        while num // 10 != 0:
            num = process(self, num)
        
        return num