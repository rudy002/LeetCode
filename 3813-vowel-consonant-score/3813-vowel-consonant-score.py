class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        
        vowel = ["a", "e", "i", "o", "u"]
        c, v = 0, 0

        for i in range(len(s)):
            if s[i] in vowel:
                v+=1
            elif s[i].isdigit() or s[i].isspace():
                continue
            else:
                c+=1
        
        if c > 0:
            return math.floor(v / c)
        else:
            return 0
            
