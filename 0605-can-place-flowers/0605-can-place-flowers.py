class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        zero = 1
        count = 0

        for i in flowerbed:
            if i == 0:
                zero+=1

            else: 
                count+= (zero - 1) //2
                zero = 0
        count += zero //2

        if count >=n:
            return True
        else:
            return False