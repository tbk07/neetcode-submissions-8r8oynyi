class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        rem_count= 0
        r = 0
        while r < len(nums):
            if nums[r] == 0:
                nums.remove(nums[r])
                rem_count += 1
            else:
                r += 1
        for _ in range(rem_count):
                nums.append(0)
                

            
                
        