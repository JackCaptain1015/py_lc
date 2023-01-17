class Solution:
    '''
    动规，与买卖股票最佳时机1相比，这题多了多次买卖。动规最重要得就是想清楚数据得状态，
    比如这里ansArr维度一表示得天数，维度二中0表示得当天不持有股票下得最大收益，1表示当天
    持有股票下得最大收益，所以在[i][0]下，相当于昨天就不持有股票或者昨天持有股票，然后今天卖掉
    股票，即昨天持有股票得收益+今天收入，所以是ansArr[i-1][1]+prices[i]。同理得ansArr[i][1]。
    '''
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices);
        ansArr = [[0]*2 for i in range(size)];
        ansArr[0][0] = 0;
        ansArr[0][1] = -prices[0];
        for i in range(1,size):
            ansArr[i][0] = max(ansArr[i-1][0],ansArr[i-1][1]+prices[i]);
            ansArr[i][1] = max(ansArr[i-1][1],ansArr[i-1][0]-prices[i]);
        return ansArr[size-1][0];
