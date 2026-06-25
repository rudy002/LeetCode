class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height) - 1
        left = 0
        right = len(height) - 1
    
        while left<right:
            temp_water = min(height[left], height[right]) * (right - left)
            if temp_water > max_water:
                max_water = temp_water
            
            if height[left] > height[right]:
                right -=1
            else:
                 left+=1
        
        return max_water