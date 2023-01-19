from typing import List


class Solution:
    '''
    动规，arr里元素表示着第i天能偷到的最多的钱，而第i天能偷盗的前主要由前一天偷没偷决定，所以
    转移方程为arr[i]= max(arr[i-1],arr[i-2]+nums[i]).
    动规的代码中不会涉及递归，更多的是数组+循环+max判断.
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0];
        arr = [0]*len(nums);
        arr[0] = nums[0];
        arr[1] = max(nums[0],nums[1]);
        for i in range(2,len(nums)):
            arr[i] = max(arr[i-1],arr[i-2]+nums[i]);
        return arr[-1];