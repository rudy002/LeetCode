class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        odd = False
        res = 0
        
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
        
        print(count)
        
        for v in count.values():
            if v % 2 == 0:
                res+=v
            else:
                res += v - 1
                odd = True
        
        if odd:
            return res + 1
        else:
            return res

        
        


