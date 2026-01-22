class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        res = ""

        for i in s:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1


        for k, v in count.items():
            if v == 1:
                res = k
                break

        for i in range(len(s)):
            if s[i] == res:
                return i
        
        return -1 