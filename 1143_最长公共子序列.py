class Solution:
    '''
    动规，将两个字符串一起看作一个二维数组，arr[i][j]即text1[0:i]与text2[0:j]
    之间的最长公共子序列长度。因此边界情况为0，如果i,j下标的字符串相等，那么
    arr[i][j]就为arr[i-1][j-1] + 1，否则就取前面的最长公共子序列。
    （注意，因为text中下标是0开始的，而arr因为边界计算，下标是从1开始的，所以
    i,j既然从1开始，那么text取字符串时候就要-1）
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2);
        arr = [[0]*(n+1) for i in range(m+1)];
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1;
                else:
                    arr[i][j] = max(arr[i][j-1],arr[i-1][j]);
        return arr[m][n];