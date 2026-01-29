class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        res = []
        maxi = len(candyType) // 2
        
        for i in candyType:
            if i in res:
                continue
            else:
                res.append(i)
        
        if maxi<= len(res):
            return maxi
        else: 
            return len(res)