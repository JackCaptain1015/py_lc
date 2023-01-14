class Solution:
    '''
    题目关键描述了当下标为-1或n时值为负无穷，如果不封装get(i)的话，二分查找
    中边界条件将很难处理。二分逻辑主要是从mid位置往值大的地方走，因为既然边界
    最小，那么往值大的地方走必然存在峰值。最后注意二分中left一定是<=right，
    而不是<,因为如果是<的话，会漏掉刚好答案就在当前left或right位置上的情况。
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        def get(i):
            if i == -1 or i == len(nums):
                return float("-inf");
            return nums[i];

        left,right = 0,len(nums)-1;
        mid = 0;
        while left <= right:
            mid = (left+right) >> 1;
            if get(mid) < get(mid+1):
                left = mid+1;
            elif get(mid) < get(mid-1):
                right = mid-1;
            else:
                return mid;
        return mid;

