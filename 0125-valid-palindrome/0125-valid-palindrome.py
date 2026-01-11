class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = s.split()
        result = ("".join(x for x in s if x.isalnum()))
        result = result.lower()
        right = len(result) - 1

        if (result == ""):
            return True

        for left in range(len(result)):
            if ((right - left) in [1,0]):
                if(result[right] == result[left]):
                    return True
                else:
                    return False
            
            if(result[left] == result[right]):
                right-=1
            else:
                return False
