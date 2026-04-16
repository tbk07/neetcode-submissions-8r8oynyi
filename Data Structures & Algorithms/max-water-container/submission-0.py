class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = 0
        for i in range(len(heights)):
            for j in range(i+ 1,len(heights)):
                sol = max(sol,min(heights[i],heights[j])*(j-i))
        return sol


        