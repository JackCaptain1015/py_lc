from typing import List
class Solution:
    '''
    排序后，子数组会按照第一个元素进行排序，这样能合并的数组就会挨在一起。
    但是也会出现[0,3],[0,1]这样的情况，所以合并时候也要按照max进行对比，
    取最大的右边元素进行合并
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]);
        ansArr = [];
        for temp in intervals:
            if not ansArr or ansArr[-1][1] < temp[0]:
                ansArr.append(temp);
            else:
                ansArr[-1][1] = max(ansArr[-1][1],temp[1]);
        return ansArr;
