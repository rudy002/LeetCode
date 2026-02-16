class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        count = {}
        res = []
        for i in bulbs:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
            
        for k, v in count.items():

            if v % 2 != 0:
                res.append(k)


        res.sort()
        return res