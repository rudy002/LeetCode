class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        res = ""

        for row in range(numRows):
            increment = 2 * (numRows -1)

            # cette boucle marche parfaitement pour la premiere et la derniere ligne.
            for i in range(row, len(s), increment):
                res += s[i]

                # il ne faut pas oublier de prendre en compte les lignes du milieu car ils ont des valeurs supplementdaire de la formule (2* (numRow) -1) - 2R
                # le dernier and est une verification que je suis dans le range. que la valeur existe
                if (row > 0 and row < numRows -1 and i+increment - 2*row < len(s)):
                    res += s[i+increment - 2*row]
        

        return res
