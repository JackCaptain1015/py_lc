from typing import List


class Solution:
    '''
    滑动窗口，细节很重要，一定是循环嵌套循环，并且+nums[right]要在最前面
    （最重要arrSum的新增要在left移动之前，不然arrSum最后一个加上了，right也等于size了，直接跳出循环了）
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0,0;
        size = len(nums);
        ans = float("inf");
        arrSum = 0;
        while right < size:
            arrSum += nums[right];
            while target <= arrSum:
                ans = min(ans,right-left+1);
                arrSum -= nums[left];
                left += 1;
            right += 1;
        return 0 if ans == float("inf") else ans;

s=Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]));