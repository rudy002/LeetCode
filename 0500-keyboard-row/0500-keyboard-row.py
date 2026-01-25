class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []

        for word in words:
            w = word.lower()

            if set(w).issubset(row1) or \
               set(w).issubset(row2) or \
               set(w).issubset(row3):
                res.append(word)

        return res
