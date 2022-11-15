class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pre_dp0 = 0  # 前一天没有股票时的最大获利
        pre_dp1 = -prices[0]  # 前一天持有股票时的最大获利

        for i in range(1, n):
            #比较前一天获利与前一天持有股票后今天卖出的最大利润之间，谁最大
            dp0 = max(pre_dp0, pre_dp1 + prices[i])
            #比较前一天持有股票的利润与前一天最大获利并且今天买入股票之间，谁获利最大
            dp1 = max(pre_dp1, pre_dp0 - prices[i])
            pre_dp0 = dp0
            pre_dp1 = dp1

        return pre_dp0
