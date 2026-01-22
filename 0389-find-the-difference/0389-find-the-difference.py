class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for i in t:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
        
        for i in s:
            if i in count:
                count[i]-=1
        
        res = ""

        for k, v in count.items():
            if v>0:
                res += k

        return res