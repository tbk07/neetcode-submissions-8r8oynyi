class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lfs = set()
        for i in range(len(nums)):
            if nums[i] in lfs:
                return True
            else:
                lfs.add(nums[i])
        return False
        