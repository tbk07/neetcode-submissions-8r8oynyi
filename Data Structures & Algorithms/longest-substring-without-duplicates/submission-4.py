class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        set1 =[]
        for r in range(len(s)):
            
            if s[r] in set1:
                l+=1
            set1.append(s[r])
            longest = max(longest, r - l + 1)

        return longest 

            
        