class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"
        
        hexa = ""
        dico = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
        }

        if num < 0:
            num = 2**32 - abs(num)

        while num > 0:
            carry = num % 16
            num//=16
            hexa+=str(dico[carry])


        return hexa[::-1]
