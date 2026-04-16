class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        longest = 0 
        max_frq = int()
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            window_size = r -l + 1
            max_frq = max(max_frq, count[s[r]])
            if window_size - max_frq > k:
                count[s[r]] -= 1
                l += 1
            longest = max(longest, r - l +1)

        return longest 


                

