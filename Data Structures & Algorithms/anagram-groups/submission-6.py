class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newlist = defaultdict(list)
        for word in strs:
            sorted_str = "".join(sorted(word))
            newlist[sorted_str].append(word) 

        return [x for x in newlist.values()]