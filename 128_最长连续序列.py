from typing import List


class Solution:
    '''
    字典，如果用in nums判断的话，会超时，毕竟序列的in是遍历的。
    这里的时间复杂度为n，主要是因为num-1在addMap中的时候，会跳过这个元素，而放到下个元素计算，最后
    计算的次数为元素个数。另外要注意，因为num-1 not in addMap时候，这个num元素已经计算长度了，所以
    tempAns初始化为1.
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0;
        addMap = set(nums);
        ans = 0;
        for num in nums:
            if num-1 not in addMap:
                tempAns = 1;
                while num+1 in addMap:
                    tempAns += 1;
                    num += 1;
                ans = max(ans,tempAns);
        return ans;
