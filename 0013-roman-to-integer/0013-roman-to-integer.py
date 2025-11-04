class Solution:
    def romanToInt(self, s: str) -> int:
        
        dico = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)-1):
            if dico[s[i]] >= dico[s[i+1]]:
                result += dico[s[i]]
            else:
                result -= dico[s[i]]

        result += dico[s[len(s)-1]]
        
        return result

