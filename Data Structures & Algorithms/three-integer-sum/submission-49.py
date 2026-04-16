class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        possible_sols = []
        
        for i in range(len(nums) - 2):
            # If the smallest number is greater than 0, we can never sum to 0. Early exit!
            if nums[i] > 0:
                break
                
            # Correctly skip duplicates for the 'i' index
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    # We found a valid triplet
                    possible_sols.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers inward to continue searching
                    left += 1
                    right -= 1
                    
                    # Skip any duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip any duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return possible_sols