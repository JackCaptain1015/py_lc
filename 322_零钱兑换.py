class Solution:
    '''
    动规，状态转移方程是f(n) = min(f(amount-coins))+1，
    for i in range(coin,amount+1)就是计算在这个coin下各个amount需要的
    最小硬币数，最后如果存在答案就返回
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float("inf")] * (amount+1);
        arr[0] = 0;
        for coin in coins:
            for i in range(coin,amount+1):
                arr[i] = min(arr[i],arr[i-coin]+1);
        return arr[amount] if arr[amount] != float("inf") else -1;