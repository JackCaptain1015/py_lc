from typing import List
class Solution:
    '''
    回溯法，tempArr.append是选择这个元素，然后back继续走分支，pop回溯状态，
    因为pop弹出append的元素后，相当于没选择这个元素了，所以最后的back即
    没有选择该元素的分支情况。最后i走到底后，新起一个数组往ans中添加
    （直接给tempArr的话，后面tempArr的改变会直接影响ansArr中数据）
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back(i):
            if i == len(nums):
                ansArr.append([i for i in tempArr]);
                return;
            tempArr.append(nums[i]);
            back(i+1);
            tempArr.pop();
            back(i+1)
        ansArr = [];
        tempArr = [];
        back(0);
        return ansArr;
