class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = 0
        sufix = 0
        total_water_trapped = 0
        for i in range(len(height) -1 ):
            prefix = max(height[:i+1])
            suffix = max(height[i:])
            water_traped_at_i = min(prefix,suffix) - height[i]
            total_water_trapped += water_traped_at_i
        return total_water_trapped
            
