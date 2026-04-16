class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = prices[0]
        for i in prices:
            maxp = max(maxp,i - minp)
            minp = min(minp, i)
        return maxp