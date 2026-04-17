class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1 = {}
        for i in range(len(t)):
            dict1[t[i]] = dict1.get(t[i],0) +1
        
        
        ans =   []
        ansLen = float("infinity")

        for i in range(len(s)):
            countS = {}
            for j in range(i,len(s)):
                countS[s[j]] = countS.get(s[j], 0) +1 
                flag = True
                for c in dict1:
                    if dict1[c] > countS.get(c, 0):
                        flag = False
                        break
                    if flag and (j - i + 1) < ansLen:
                        ansLen = j - i +1
                        ans = [i,j]
        
        l, r = ans
        return s[l :r +1] if ansLen != float("infinity") else ""
        