class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        vowel_in = []
        new_s = ""
        
        for i in s:
            if i in vowel:
                vowel_in.append(i)
        n = len(vowel_in) -1
        for i in range(0 , len(s) , 1):
            if s[i] in vowel:
                new_s += vowel_in[n]
                n-=1
            else:
                new_s += s[i]
        
        return new_s
        
        return s
                

