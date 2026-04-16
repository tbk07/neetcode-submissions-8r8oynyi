class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasmap = set()
        for n in nums:
            if n in hasmap:
                return True
            hasmap.add(n)
        return False    
        
        
         