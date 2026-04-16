class Solution:
    def maxArea(self, heights: List[int]) -> int:
        resu = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            resu = max(resu, min(heights[left], heights[right]) * (right-left))
            if heights[left] < heights[right]:
                left = left + 1
            elif heights[right] < heights[left]:
                right = right - 1  

            else:
                left += 1
                right -= 1 
        return resu

        
        