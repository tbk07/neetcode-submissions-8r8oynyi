class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = set()
        for i in nums:
            if i in my_dict:
                return True
            else:
                my_dict.add(i)
        return False  