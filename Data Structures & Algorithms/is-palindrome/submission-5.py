class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+','', s).lower()
        i = 0 
        j = len(s) -1
        return s == s[::-1]