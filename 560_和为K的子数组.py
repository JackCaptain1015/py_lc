import collections
from typing import List

'''
大佬，我从别人那里看到的分析法，nums[:i]+nums[i:j]=nums[:j]，我们需要的就是中间的nums[i:j]，令nums[i:j]=k，可以获得nums[:j]-k = nums[:i] ，就是当前前缀和减去目标得到的前方前缀和的数量（绝大部分情况下前缀和的数量为1，有0或者负数的时候才会出现大于1），这种分析可以很好得理解为什么要搜索前缀和，同时，哈希表的搜索复杂度是O(1)，所以使用哈希表


'''
class Solution:
    '''
    前缀和，sumMap中key为nums[:i]的和，val为该和出现的次数。
    因为球的是nums[i:j]之间和为k的连续子序列数，所以nums[i:j] = nums[:j]-nums[:i] = k，
    因此key则是nums[:i] = nums[:j] - k，其中nums[:j]则为sum。
    所以如果sumMap.get(sum-k)存在，即这个连续子序列满足和为k。（连续由遍历保证）。
    又因为相同和的子序列可能出现多个,所以答案为所有下标结尾的和为 k 的子序列个数之和，
    即ans += sumMap.get(sum-k)，而不是ans +=1。
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0;
        ans = 0;
        sumMap = collections.defaultdict(int);
        sumMap[0] = 1;
        for i in range(len(nums)):
            sum += nums[i];
            if sumMap.get(sum-k):
                ans += sumMap.get(sum-k);
            sumMap[sum] += 1;
        return ans;


print(Solution().subarraySum([1,-1,2,3,-3],0))