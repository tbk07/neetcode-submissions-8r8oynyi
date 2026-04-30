class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frqq = [[] for i in range(len(nums)+1)]
        newdict = {}
        for i in nums:
            newdict[i] = newdict.get(i,0) +1
        for i,c in newdict.items():
            frqq[c].append(i)

        output = []
        for i in range(len(frqq) -1, 0 ,-1):
            for n in frqq[i]:
                output.append(n)
                if len(output) == k:
                    return output     