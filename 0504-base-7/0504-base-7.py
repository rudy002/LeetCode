class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        copy = num

        while abs(num) >0:
            carry = abs(num) % 7
            num = abs(num) // 7
            res += str(carry)
        if copy >= 0:
            return res[::-1]
        else:
            return "-" + res[::-1]