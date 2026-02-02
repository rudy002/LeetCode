class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dico1 = {name:i for i, name in enumerate(list1)}
        min_sum = 10000

        res = []

        for j, name in enumerate(list2):
            if name in dico1:
                s = dico1[name] + j
                if s < min_sum:
                    min_sum = s
                    res = [name]
                elif s == min_sum:
                    res.append(name)
        
        return res