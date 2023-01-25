class Solution:
    '''
    动规，因为需要从正负方面来想，如果是负数的话，那希望越小越好，
    到时候负负得正就越大。
    maxArr与minArr的下标表示以i下标为末尾的子序列的最大或最小乘积。
    '''
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums);
        maxArr,minArr= [0]*size,[0]*size;
        maxArr[0],minArr[0] = nums[0],nums[0];
        for i in range(1,size):
            maxArr[i] = max(maxArr[i-1]*nums[i],max(nums[i],minArr[i-1]*nums[i]));
            minArr[i] = min(minArr[i-1]*nums[i],min(nums[i],maxArr[i-1]*nums[i]));
        return max(maxArr);