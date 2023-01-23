from typing import List


class Solution:
    '''
        回溯，循环是选择每个数字的可能性，back(temp,i)而不是back(temp,i+1)，是因为每个下标都可以重复选择
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(sum,idx):
            if sum == target:
                ansArr.append([i for i in pathArr]);
                return ;
            if idx >= len(candidates):
                return ;
            for i in range(idx,len(candidates)):
                temp = sum + candidates[i];
                if temp <= target:
                    pathArr.append(candidates[i]);
                    back(temp,i);
                    pathArr.pop();
        ansArr = [];
        pathArr = [];
        back(0,0);
        return ansArr;
