from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dico = {}

        # Compter occurrences
        for x in nums:
            dico[x] = dico.get(x, 0) + 1

        # Trouver le dupliqué (valeur == 2)
        dupplique = None
        for k, v in dico.items():
            if v == 2:
                dupplique = k
                break

        # Trouver le manquant (clé absente entre 1 et n)
        manquant = None
        n = len(nums)
        for i in range(1, n + 1):
            if i not in dico:
                manquant = i
                break

        return [dupplique, manquant]
