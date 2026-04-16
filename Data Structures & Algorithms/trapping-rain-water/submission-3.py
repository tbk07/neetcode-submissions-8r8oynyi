class Solution:
    def trap(self, height: List[int]) -> int:
        water_capacity = 0
        for i in range(1,len(height) -1 ):
            
            left = height[i]
            for j in range(0,i):
                left = max(left, height[j])
            right = height[i]
            for j in range(i +1,len(height) ):
                right = max(right, height[j])
            
            water_capacity += min(left,right) - height[i]

        return water_capacity        