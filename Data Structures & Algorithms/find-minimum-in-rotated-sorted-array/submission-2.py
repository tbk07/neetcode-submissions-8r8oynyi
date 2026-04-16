class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimumval = nums[0]
        for i in range(len(nums)):
            minimumval = min(minimumval,nums[i])
        return minimumval
        