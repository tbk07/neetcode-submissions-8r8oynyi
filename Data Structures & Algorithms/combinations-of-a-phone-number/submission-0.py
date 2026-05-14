class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyword_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = [""]
        for digit in digits:
            temp = []
            for x in res:
                for c in keyword_dict[digit]:
                    temp.append(x + c)
            res = temp 

        return res 



