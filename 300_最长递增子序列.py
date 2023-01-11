class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            动态规划，主要思路是计算之前的子序列的长度
            （注意初始化长度为1，用于刚开始时候的长度），
            然后计算当前序列长度时候跟前序列长度进行max对比，
            最后计算出最终所有子序列的长度，获取最大值
        '''
        dp = [];
        for i in range(len(nums)):
            dp.append(1);
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1);
        return max(dp);