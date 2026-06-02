class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        groups = []
        result = [""]

        for d in digits: 
            groups.append(buttons[d])

        for group in groups:
            result =  [x + y for x in result for y in group]
        
        return result
