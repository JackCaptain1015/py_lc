from typing import List


class Solution:
    '''
        回溯，第一个递归是把指针遍历到尾部，这样递归回来以后会从尾部一直递归回头部，
        然后值得注意的是ansArr的append要给新的数组，避免引用，最后要注意回溯状态删除tempArr元素时，
        要使用tempArr的方法，使用tempArr = tempArr[:len(tempArr)-1]的话，是不会执行的，
        估计是python编译器判断这个变量最后没用，所以直接就没执行
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def cal(arr,target,tempArr,idx):
            if idx == len(arr):
                return;
            if target == 0:
                ansArr.append([temp for temp in tempArr]);
                return;
            cal(arr,target,tempArr,idx+1);
            if target - arr[idx] >= 0:
                tempArr.append(arr[idx]);
                cal(arr,target-arr[idx],tempArr,idx);
                tempArr.pop();
        ansArr = [];
        cal(candidates,target,[],0);
        return ansArr;
