class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        count = {}
        longest = 0
        for r in range(len(s)-1):        
            count[s[r]] = count.get(count[s[r]],0) +1
            while s[r] == s[l]:
                r +=1
                longest = max(longest, r - l )
                

            if s[r] != s[l]:
                l+=1
                if k >0:
                    s[r] = max(count.value())
                
        
        
        
        return longest


                


            
