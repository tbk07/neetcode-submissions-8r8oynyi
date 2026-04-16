class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visted:
                return [visted[diff], i]
            else:
                visted[nums[i]] = i 
        