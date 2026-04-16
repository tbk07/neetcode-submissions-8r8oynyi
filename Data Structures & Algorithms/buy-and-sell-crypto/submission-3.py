class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro=0
        minbuy= prices[0]

        for i in prices:
            maxpro = max(maxpro,i - minbuy )
            minbuy = min(minbuy, i)
        return maxpro


