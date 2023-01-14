from typing import List
class Solution:
    '''
    动规计算dp[i][j]为右下角情况下的复合正方形的最大边长（正方形的计算是隐含在min中的，
    因为dp是复合正方形的最大变成，即最小为1，即dp[i][j]本身最小正方形，如果为2也说明该位置下有个边长为2的正方形）
    '''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0;
        rows,cols = len(matrix),len(matrix[0]);
        dp = [[0]*cols for i in range(rows)];
        maxAns = 0;
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1;
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1;
                    maxAns = max(maxAns,dp[i][j]);
        return maxAns*maxAns;
