class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        indexzero = 0
        num = 0
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        i = 0

        int_min = -2**31
        int_max = 2 ** 31 -1

        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0

        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            return 0
    
            
            
        while i < len(s) and s[i] in digits:
            num = num * 10 + int(s[i])
            i+=1
            if sign * num < int_min:
                return int_min
            elif sign * num > int_max:
                return int_max
        
        return sign * num


