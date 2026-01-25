class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res = ""
        carry = 0
        if len(num1)>len(num2):
            num2 = num2.zfill(len(num1))
        elif len(num2)>len(num1):
            num1 = num1.zfill(len(num2))

        for i in range(len(num1)-1,-1,-1):
            adding = int(num1[i]) + int(num2[i]) + carry
            res += str(adding % 10)
            carry = adding // 10
        
        if carry > 0:
            return str(carry) + res[::-1]
        else:
                return res[::-1]
        
