class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:       
            res = []
            for i in range(len(nums)):
                left = 0
                right = len(nums) -1
                sums = 1
                while left < right:
                    if i > left:
                        sums = sums * nums[left]
                        left += 1
                    elif i < right:
                        sums = sums * nums[right]
                        right -= 1
                res.append(sums)
            return res