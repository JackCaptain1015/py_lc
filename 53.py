class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #动规思路中的f(i-1)是已包含nums[i-1]为末尾元素的最大和解
        #换句话来说，f(i-1)舍弃了不是nums[i-1]为末尾元素的最大和解的其他前面的元素
        #因此f(i)只需要判断max(f(i-1)+nums[i],nums[i])
        preSum,res = 0,nums[0];
        for num in nums:
            preSum = max(preSum+num,num);
            res = max(res,preSum);
        return res;
