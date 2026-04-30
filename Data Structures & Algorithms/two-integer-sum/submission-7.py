class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            to_find = target - nums[i]
            for j in range(len(nums)):
                if to_find == nums[j]:
                    return [i,j]
            

