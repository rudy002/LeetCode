class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        scores = sorted(score, reverse=True)
        order = {}
        
        for i in range(len(score)):
            if i == 0:
                order[scores[i]] = "Gold Medal"
            elif i == 1:
                order[scores[i]] = "Silver Medal"
            elif i == 2:
                order[scores[i]] = "Bronze Medal" 
            else:
                order[scores[i]] = str(i+1)

        res = []
        
        for i in score:
            res.append(order[i])

        return res


        