class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin = format(x, '032b')  
        ybin = format(y, '032b')
        count = 0

        for i in range(len(xbin)):
            if xbin[i] != ybin[i]:
                count+=1
        
        return count

        