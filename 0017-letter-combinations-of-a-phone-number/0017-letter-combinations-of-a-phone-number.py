class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if digits == "":
            return []

        if len(digits) == 1:
            return phone[digits[0]]

        res = ['']

        for digit in digits:
            letter = phone[digit]
            new_res = []

            for x in res:
                for y in letter:
                    new_res.append(x + y)
            
            res = new_res
        
        return res
        