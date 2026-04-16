class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        possible_sols = []
        
        for i in range(len(nums) -2 ):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) -1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums < 0:
                    left = left +1
                if sums > 0:
                    right = right - 1
                if sums == 0:
                    possible_sols.append([nums[i],nums[left],nums[right]])
                    left = left +1
                    right = right - 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return possible_sols
        
        