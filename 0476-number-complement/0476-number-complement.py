class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        reverse = ""

        for bit in binary:
            if bit == "0":
                reverse += "1"
            else:
                reverse += "0"

        return int(reverse, 2)
