class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','', s)
        s = s.lower()
        s_r = s[::-1]
        s_r = s_r.strip()
        if s_r == s:
            return True 
        else:
            return False
        