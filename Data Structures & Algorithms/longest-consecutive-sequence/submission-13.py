
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        best = 1
        i = 0
        nums = sorted(set(nums))
        if nums == []:
            return 0

        
        while i < len(nums)-1:
            if nums[i] + 1 == nums[i +1]:
                count+=1
                best = max(best, count)
            else:
                count = 1
            i +=1
                
                
        return best 


        