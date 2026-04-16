class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            pivot_point = (left + right ) //2
            res = min(res, nums[pivot_point]) 
            if nums[pivot_point] < nums[left]:
                right = pivot_point - 1
            else:
                left = pivot_point + 1
        return res
        