class Solution:
    def countSegments(self, s: str) -> int:
        temp = ""
        ls = []

        for i in range(len(s)):
            if s[i]==" ":
                if temp != "":
                    ls.append(temp)
                temp = "" 
            else:
                temp+=s[i]
        
        if temp != "":
            ls.append(temp)
        
        return len(ls)