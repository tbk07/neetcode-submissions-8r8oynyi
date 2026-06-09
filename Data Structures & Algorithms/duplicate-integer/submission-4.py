class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_pairs = set()
        for i in nums:
            if i in unique_pairs:
                return True
            unique_pairs.add(i)
        return False


        