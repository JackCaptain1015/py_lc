from typing import List


class Solution:
    '''
    动规，求最大、最小次数，一般来说都是动规。
    这里arr[i]表示金额为i时候的组合数。所以金额为0时候表示不选，默认为1.
    两层循环表示各个金额在选中硬币下的组合数，所以arr[i] += arr[i-coin]
    表示i金额在所有硬币下的组合数。并且因为coin遍历是往后的，所以不会重复
    计算。
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0]*(amount+1);
        arr[0] = 1;
        for coin in coins:
            for i in range(coin,amount+1):
                arr[i] += arr[i-coin];
        return arr[amount];


print(Solution().change(5,[1,2,5]));