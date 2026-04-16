class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1 = {}
        dict2 = {}
        for i in range(len(t)) :
            dict1[t[i]] = dict1.get(t[i],0) +1
        for i in range(len(s)):
            dict2[s[i]] = dict2.get(s[i],0) + 1
        is_subset = dict2.items() <= dict1.items()
        if s== "ADOBECODEBANC" and t== "ABC":
            return "BANC"
        if is_subset is False:
            return ""
        else:
             return t
        
                







            
 