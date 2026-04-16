class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list11 = defaultdict(list)
        for i in strs:
            strs_sorted = "".join(sorted(i))
            list11[strs_sorted].append(i)
        
        return [x for x in list11.values()]

        