class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) !=len(t): return False

        for letter1 in t:
            for letter2 in s:
                if letter1==letter2:
                    s = s.replace(letter1, "", 1)
                    break
        
        if len(s) == 0: return True
        else: return False