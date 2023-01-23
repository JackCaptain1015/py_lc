import collections
from typing import List


class Solution:
    '''
        回溯，与39题不一样的是，这题不可以重复选择相同下标元素，以及排除相同组合，所以开头先对原数组进行了排序，
        这样相同的的元素就在一起了，所以当循环时候，如果在该分支下，剩下的带选择元素中如果有相同元素就跳过
        （因为选择了相同元素的头一个，所以剩下的如果不符合条件就没必要选了，如果符合条件的话，会回溯进入下一个分支）。
        另外，与39题不同的是，因为39题元素是可以重复选的，所以是back(temp,i)，而这里元素是只能选择一次的，所以
        是back(temp,i+1)
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(sum,idx):
            if sum == target:
                ansArr.append([i for i in pathArr]);
                return ;
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue;
                temp = candidates[i] + sum;
                if temp <= target:
                    pathArr.append(candidates[i]);
                    back(temp,i+1);
                    pathArr.pop();

        ansArr = [];
        pathArr = [];
        candidates = sorted(candidates);
        back(0,0);

        return ansArr;

print(Solution().combinationSum2([1,6,1],8))
